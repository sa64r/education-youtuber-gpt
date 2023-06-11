""" This script populates the database with the transcriptions of the videos """
import scrapetube
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.chromadb_utils import get_client


# MANUALLY SET THESE VALUES BEFORE RUNNING THE SCRIPT
CHANNEL_ID = "UC_mYaQAE6-71rjSN6CeCA-g"
CHANNEL_NAME = "NeetCode"  # cannot have spaces


# pull youtube videos from channel
def get_youtube_videos(channel_id):
    """Returns a list of video ids from a channel"""
    return list(map(lambda video: video["videoId"], scrapetube.get_channel(channel_id)))


# get full transcription of video
def get_full_transcription_of_video(video_id):
    """Returns the full transcription of a video"""
    transcription = YouTubeTranscriptApi.get_transcript(video_id)
    full_transcription = "".join(list(map(lambda x: x["text"] + " ", transcription)))
    return full_transcription


# split transcription into chunks
def split_transcription_into_chunks(transcription: str):
    """Returns a list of chunks of a transcription"""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    return text_splitter.split_text(text=transcription)


# create channel collections
def create_channel_collection(channel_name: str):
    """Returns a collection for a channel"""
    return get_client(".chromadb").get_or_create_collection(channel_name)


# add list of transcription snippets to collection
def add_list_of_text_to_collection(text_list: list[str], video_id: str, collection):
    """Adds a list of text snippets to a collection"""
    collection_count = collection.count()
    collection.add(
        documents=text_list,
        metadatas=[{"video_id": video_id} for _ in text_list],
        ids=[
            str(n)
            for n in list(range(collection_count, collection_count + len(text_list)))
        ],
    )


def main():
    """Main function"""
    print("starting")

    # get video ids from channel
    video_ids = get_youtube_videos(CHANNEL_ID)
    print(video_ids)

    # create channel collection
    collection = create_channel_collection(CHANNEL_NAME)
    print(collection.name)

    # add video transcriptions to collection
    for video_id in video_ids:
        try:
            add_list_of_text_to_collection(
                split_transcription_into_chunks(
                    get_full_transcription_of_video(video_id)
                ),
                video_id,
                collection,
            )
        except RuntimeError:
            print(f"failed on {video_id}")
        print(collection.count())

    print("done")


main()
