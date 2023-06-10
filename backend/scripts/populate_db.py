# MANUALLY SET THESE VALUES BEFORE RUNNING THE SCRIPT
CHANNEL_ID = "UCcc6bSEKsxrlDmipLQjbGHg"
CHANNEL_NAME = "SA64R"

import scrapetube
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter

from backend.utils.chromadb import get_client


# pull youtube videos from channel
def get_youtube_videos(channel_id):
    return list(map(lambda video: video["videoId"], scrapetube.get_channel(channel_id)))


# get full transcription of video
def get_full_transcription_of_video(video_id):
    transcription = YouTubeTranscriptApi.get_transcript(video_id)
    full_transcription = "".join(list(map(lambda x: x["text"] + " ", transcription)))
    return full_transcription


# split transcription into chunks
def split_transcription_into_chunks(transcription: str):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    return text_splitter.split_text(text=transcription)


# create channel collections
def create_channel_collection(channel_name: str):
    return get_client().get_or_create_collection(channel_name)


# add list of transcription snippets to collection
def add_list_of_text_to_collection(text_list, collection):
    collection_count = collection.count()
    collection.add(
        documents=text_list,
        ids=[
            str(n)
            for n in list(range(collection_count, collection_count + len(text_list)))
        ],
    )


def main():
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
                collection,
            )
        except:
            print("failed on %s" % video_id)
        print(collection.count())

    print("done")


main()
