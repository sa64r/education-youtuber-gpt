# connect to database
import chromadb

from chromadb.config import Settings

client = chromadb.Client(
    Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="backend/.chromadb",  # Optional, defaults to .chromadb/ in the current directory
    )
)


def get_client():
    return client
