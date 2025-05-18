import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()  # loads .env file with your API key

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("Please add your OPENAI_API_KEY to .env file")
    st.stop()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

st.title("Personal Finance Advisor")

user_input = st.text_input("Ask me anything about your personal finance:")

if user_input:
    response = llm([HumanMessage(content=user_input)])
    st.write(response.content)
