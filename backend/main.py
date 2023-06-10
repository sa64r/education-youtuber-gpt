from backend.utils.chromadb import get_client
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import os

# setup env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# load llm and chain
llm = OpenAI(temperature=0.9, openai_api_key=OPENAI_API_KEY)
chain = load_qa_chain(llm, chain_type="stuff")


class LangchainDocument:
    def __init__(self, page_content: str):
        self.page_content = page_content
        self.metadata = {}


def collections_in_db():
    return get_client().list_collections()


def query_collection(collection_name, query):
    return (
        get_client()
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


def get_answer(collection_name: str, query: str) -> str:
    db_query_response = query_collection(collection_name, query)
    langchain_documents = map_query_response_to_langchain_document(db_query_response)
    response = chain.run(input_documents=langchain_documents, question=query)

    return response
