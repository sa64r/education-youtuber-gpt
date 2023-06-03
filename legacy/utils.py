import chromadb
from chromadb.config import Settings


class LangchainDocument:
    def __init__(self, page_content: str):
        self.page_content = page_content
        self.metadata = {}


def load_chroma_client():
    return chromadb.Client(
        Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory="chroma_db",
        )
    )


def get_or_create_collection(collection_name: str, client):
    return client.get_or_create_collection(name=collection_name)


def query_collection(query: str, collection, n_results: int):
    return collection.query(query_texts=[query], n_results=n_results)


def map_query_response_to_langchain_document(result):
    documents = result["documents"][0]
    return list(
        map(lambda doc_text: LangchainDocument(page_content=doc_text), documents)
    )


def clear_db(client):
    client.reset()


def add_list_of_text_to_collection(text_list: list, collection):
    collection_count = collection.count()
    collection.add(
        documents=text_list,
        ids=[
            str(n)
            for n in list(range(collection_count, collection_count + len(text_list)))
        ],
    )
