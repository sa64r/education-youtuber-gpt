import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv

from utils import (
    load_chroma_client,
    query_collection,
    map_query_response_to_langchain_document,
)

client = load_chroma_client()


# setup env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


llm = OpenAI(temperature=0.9, openai_api_key=OPENAI_API_KEY)
chain = load_qa_chain(llm, chain_type="stuff")

# get collection names
collections = list(map(lambda c: c.name, client.list_collections()))


st.title("📖 Education YouTuber GPT")
youtuber = st.selectbox("Select a YouTuber", collections)

collection = client.get_collection(youtuber)

print(collection.count())

query = st.text_input("What do you want to ask?")

NUMBER_OF_RESULTS = 5

if query:
    query_result = query_collection(query, collection, NUMBER_OF_RESULTS)
    print(query_result)

    docs = map_query_response_to_langchain_document(query_result)
    response = chain.run(input_documents=docs, question=query)
    st.write(response)
