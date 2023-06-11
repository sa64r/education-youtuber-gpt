from backend.utils.chromadb import get_client
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
import os

# setup env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PERSIST_DIRECTORY = "backend/.chromadb"

# load llm and chain
llm = ChatOpenAI(temperature=0.9, openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")
chain = load_qa_chain(llm, chain_type="stuff")


class LangchainDocument:
    def __init__(self, page_content: str):
        self.page_content = page_content
        self.metadata = {}


def collections_in_db():
    return get_client(PERSIST_DIRECTORY).list_collections()


def query_collection(collection_name, query):
    return (
        get_client(PERSIST_DIRECTORY)
        .get_collection(collection_name)
        .query(query_texts=[query], n_results=5)
    )


def map_query_response_to_langchain_document(
    query_response,
) -> list[LangchainDocument]:
    documents = query_response["documents"][0]
    return list(
        map(lambda doc_text: LangchainDocument(page_content=doc_text), documents)
    )


def get_answer(collection_name: str, query: str):
    db_query_response = query_collection(collection_name, query)
    metadatas = db_query_response["metadatas"][0]
    relevant_video_id: list[str] = list(
        map(lambda metadata: metadata["video_id"], metadatas)
    )
    unique_video_ids = list(set(relevant_video_id))
    langchain_documents = map_query_response_to_langchain_document(db_query_response)
    response = chain.run(input_documents=langchain_documents, question=query)

    return response, unique_video_ids
