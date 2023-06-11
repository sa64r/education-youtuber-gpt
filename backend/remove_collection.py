from utils.chromadb import get_client

COLLECTION_NAME_TO_DELETE = "SQuotient"


# remove collection
def remove_collection(collection_name: str):
    get_client(".chromadb").delete_collection(collection_name)


def main():
    remove_collection(COLLECTION_NAME_TO_DELETE)


main()
