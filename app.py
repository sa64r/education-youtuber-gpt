import streamlit as st

from backend.main import collections_in_db, get_answer

#  title
st.title("📚📹 YouTuber GPT")

#  description
st.markdown(
    """
    This app allows you to ask questions to extract information from videos on YouTube Channels.
    """
)

open_ai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

if not open_ai_api_key:
    st.warning("Please enter your OpenAI API Key")

else:
    # select channel
    collections = collections_in_db()
    if collections:
        collection_names = list(map(lambda c: c.name, collections))

        channel = st.selectbox(
            "Select a YouTube Channel",
            collection_names,
        )

        # text input for query
        query = st.text_input("Ask a question")

        answer, relevant_video_ids = get_answer(channel, query, open_ai_api_key)

        # output
        if query:
            st.write(answer)
            st.divider()

        if query and relevant_video_ids:
            st.write("Want more information, these videos may be relevant:")
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
    else:
        st.warning("No channels uploaded.")
