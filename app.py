import os
import streamlit as st
from langchain.llms import OpenAI
from dotenv import load_dotenv

# setup env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


st.title("📖 Education YouTuber GPT")
selected_youtuber = st.selectbox(
    "Select a YouTuber",
    ("Ali Abdaal", "SA64R"),
)

prompt = st.text_input("What do you want to ask %s?" % selected_youtuber)


llm = OpenAI(temperature=0.5)
if prompt:
    response = llm(
        "Respond as if you are %s, to this prompt: %s" % (selected_youtuber, prompt)
    )

    st.write(response)
