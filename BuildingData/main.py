import chromadb
from chromadb.config import Settings

chroma_client = chromadb.Client(
    Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="chroma_db",
    )
)

# collection = chroma_client.create_collection(name="my_collection")

# collection.add(
#     documents=[
#         "To make a sandwich you need to put bread together",
#         "Building a plane is very hard",
#         "The tallest building in the world is the Burj Khalifa",
#     ],
#     ids=["1", "2", "3"],
# )

collection = chroma_client.get_collection(name="my_collection")


results = collection.query(query_texts=["is building a plane hard?"], n_results=3)

print(results)
