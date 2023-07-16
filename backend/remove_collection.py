""" Remove a collection from the database. """
from utils.chromadb_utils import get_client

COLLECTION_NAME_TO_DELETE = "Fireship"


# remove collection
def remove_collection(collection_name: str):
    """Removes a collection from the database"""
    get_client("backend/.chromadb").delete_collection(collection_name)


def main():
    """Main function"""
    remove_collection(COLLECTION_NAME_TO_DELETE)


main()
