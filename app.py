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

answer = get_answer(channel, query)

# output
if query:
    st.write(answer)
