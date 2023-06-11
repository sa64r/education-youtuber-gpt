""" ChromaDB utils """
import chromadb

from chromadb.config import Settings


def get_client(persist_directory):
    """Returns a chromadb client"""
    client = chromadb.Client(
        Settings(
            chroma_db_impl="duckdb+parquet",
            # Optional, defaults to .chromadb/ in the current directory
            persist_directory=persist_directory,
        )
    )

    return client
