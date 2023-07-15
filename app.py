""" Streamlit app for YouTuber GPT """
import streamlit as st

from backend.main import collections_in_db, get_answer, populate_db

#  title
st.title("📚📹 YouTuber GPT")

#  description
st.markdown(
    """
    This app allows you to ask questions to extract information from videos on YouTube Channels.
    """
)

with st.expander("Settings ⚙️", expanded=True):
    open_ai_api_key = st.text_input(
        "Enter your OpenAI API Key, you can get yours from"
        + " (https://platform.openai.com/account/api-keys)",
        type="password",
    )
    budget = st.slider(
        "Budget, the higher you set this value the better the response will be,"
        + " but it will cost you more",
        min_value=1,
        max_value=9,
        value=5,
        step=1,
    )


if not open_ai_api_key:
    st.warning("Please enter your OpenAI API key to use this app")

else:
    # select channel
    collections = collections_in_db()
    if collections:
        print(collections)
        collection_names = list(map(lambda c: c.name, collections))

        channel = st.selectbox(
            "Select a YouTube Channel",
            collection_names,
        )

        # text input for query
        query = st.text_input("Ask a question")

        ask_pressed = st.button("Ask")

        # output
        if query and ask_pressed:
            answer, relevant_video_ids = get_answer(
                channel, query, open_ai_api_key, budget
            )
            st.write(answer)
            st.divider()

        if query and relevant_video_ids:
            st.write("Want more information, these videos may be relevant:")
            columns = st.columns(2)

            for i in range(0, len(relevant_video_ids), 2):
                with columns[0]:
                    video_id_1 = relevant_video_ids[i]
                    video_url_1 = f"https://www.youtube.com/watch?v={video_id_1}"
                    st.video(video_url_1)

                try:
                    video_id_2 = relevant_video_ids[i + 1]
                    video_url_2 = f"https://www.youtube.com/watch?v={video_id_2}"
                    with columns[1]:
                        st.video(video_url_2)
                except IndexError:
                    pass
    else:
        st.warning("No channels uploaded, please upload a channel first.")

    # sidebar
    st.sidebar.title("Add another youtube channel")
    channel_id = st.sidebar.text_input("Enter a YouTube Channel ID")
    channel_name = st.sidebar.text_input("Enter the YouTube Channel's Name (no spaces)")
    pressed = st.sidebar.button("Add Channel")
    if channel_id and channel_name and pressed:
        st.sidebar.write("Processing channel, this may take a few minutes...")
        DONE = populate_db(channel_name, channel_id)

        if DONE:
            st.sidebar.success(f"The channel {channel_name} is successfully added!")
