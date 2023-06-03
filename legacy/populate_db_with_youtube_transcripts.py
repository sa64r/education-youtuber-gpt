from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
import scrapetube
from utils import (
    add_list_of_text_to_collection,
    get_or_create_collection,
    load_chroma_client,
)


def get_full_transcription_of_video(video_id):
    transcription = YouTubeTranscriptApi.get_transcript(video_id)
    full_transcription = "".join(list(map(lambda x: x["text"] + " ", transcription)))
    return full_transcription


def split_transcription_into_chunks(
    transcription: str,
):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    return text_splitter.split_text(text=transcription)


def get_video_is_from_channel(channel_id):
    return list(map(lambda video: video["videoId"], scrapetube.get_channel(channel_id)))


def add_channel_transcripts_to_db(youtuber_name: str, channel_id: str):
    print('Adding channel "%s" to db' % youtuber_name)
    client = load_chroma_client()

    collection = get_or_create_collection(youtuber_name, client)

    video_ids = get_video_is_from_channel(channel_id)

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
