from utils import load_chroma_client


client = load_chroma_client()

collections = client.list_collections()

print(collections[1].count())
