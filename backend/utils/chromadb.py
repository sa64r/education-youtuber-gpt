# connect to database
import chromadb

from chromadb.config import Settings


def get_client(persist_directory):
    client = chromadb.Client(
        Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=persist_directory,  # Optional, defaults to .chromadb/ in the current directory
        )
    )

    return client
