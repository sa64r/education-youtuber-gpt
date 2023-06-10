import streamlit as st

from backend.main import collections_in_db, get_answer

#  title
st.title("📚📹 YouTube Channel GPT")

#  description
st.markdown(
    """
    This app allows you to ask questions to extract information from videos on YouTube Channels.
    """
)

# select channel

collections = collections_in_db()
collectionNames = list(map(lambda c: c.name, collections))

channel = st.selectbox(
    "Select a YouTube Channel",
    collectionNames,
)

# text input for query
query = st.text_input("Ask a question")

answer, relevant_video_ids = get_answer(channel, query)

# output
if query:
    st.write(answer)
    st.divider()


if query and relevant_video_ids:
    st.write("Want more information, check out these recommended videos:")
    columns = st.columns(2)

    for i in range(0, len(relevant_video_ids), 2):
        with columns[0]:
            video_id_1 = relevant_video_ids[i]
            video_url_1 = "https://www.youtube.com/watch?v=%s" % video_id_1
            st.video(video_url_1)

        try:
            video_id_2 = relevant_video_ids[i + 1]
            video_url_2 = "https://www.youtube.com/watch?v=%s" % video_id_2
            with columns[1]:
                st.video(video_url_2)
        except:
            pass
