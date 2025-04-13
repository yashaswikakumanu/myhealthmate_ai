from crewai import Agent
from langchain_openai import ChatOpenAI
import streamlit as st
import os

# ✅ Securely use OpenAI key from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(
    model="gpt-4o-mini",  
    temperature=0.2
)

medical_parser_agent = Agent(
    role="Medical Report Parser",
    goal="Extract relevant metrics (BP, Sugar, Cholesterol, etc.) and conditions from medical PDFs",
    backstory="An expert healthcare data analyst trained to extract structured clinical insights",
    llm=llm
)