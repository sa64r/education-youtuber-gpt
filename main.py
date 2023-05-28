import os

# for ui
import streamlit as st

# import openAI as LLM service
from langchain.llms import OpenAI

# import openAI apikey
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


st.title("😁 Sagar GPT")
prompt = st.text_input("Enter your prompt now")
temperature = st.slider("Temperature", 0.0, 1.0, 0.9, 0.01)


llm = OpenAI(temperature=temperature)
if prompt:
    response = llm(prompt)

    st.write(response)
