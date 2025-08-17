from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.llms import OllamaLLM

import streamlit as st
import os
from dotenv import load_dotenv

# Langsmith
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = 'true'

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful assistant. Please respond to the user queries.'),
        ("user", "Question: {question}")
    ]
)

# Streamlit
st.title("Demo Chatbot")
input_text = st.text_input("Search the topic U want")

# Ollmama LLAMA2 LLM Model
llm = OllamaLLM(model='llama2')
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Waiting for user input:
if input_text:
    st.write(chain.invoke({"question":input_text}))