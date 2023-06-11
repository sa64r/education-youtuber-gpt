""" This module contains the main logic for the backend. """
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

# pylint: disable=import-error
from backend.utils.chromadb_utils import get_client


# setup env
load_dotenv()
PERSIST_DIRECTORY = "backend/.chromadb"


# pylint: disable=too-few-public-methods
class LangchainDocument:
    """A document for the langchain"""

    def __init__(self, page_content: str):
        self.page_content = page_content
        self.metadata = {}


def collections_in_db():
    """Returns a list of collections in the database"""
    return get_client(PERSIST_DIRECTORY).list_collections()


def query_collection(collection_name, query, budget):
    """Returns a query response from the database"""
    return (
        get_client(PERSIST_DIRECTORY)
        .get_collection(collection_name)
        .query(query_texts=[query], n_results=budget)
    )


def map_query_response_to_langchain_document(
    query_response,
) -> list[LangchainDocument]:
    """Returns a list of LangchainDocuments from a query response"""
    documents = query_response["documents"][0]
    return list(
        map(lambda doc_text: LangchainDocument(page_content=doc_text), documents)
    )


def get_answer(collection_name: str, query: str, openai_api_key: str, budget: int):
    """Returns a plain text answer with the video ids that were used to generate it"""
    db_query_response = query_collection(collection_name, query, budget)
    metadatas = db_query_response["metadatas"][0]
    relevant_video_id: list[str] = list(
        map(lambda metadata: metadata["video_id"], metadatas)
    )
    unique_video_ids = list(set(relevant_video_id))
    langchain_documents = map_query_response_to_langchain_document(db_query_response)

    # load llm and chain
    llm = ChatOpenAI(
        temperature=0.9, openai_api_key=openai_api_key, model="gpt-3.5-turbo"
    )
    chain = load_qa_chain(llm, chain_type="stuff")

    response = chain.run(input_documents=langchain_documents, question=query)

    return response, unique_video_ids
