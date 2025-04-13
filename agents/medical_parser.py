from crewai import Agent
from langchain_openai import ChatOpenAI
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",  
    temperature=0.2
)

medical_parser_agent = Agent(
    role="Medical Report Parser",
    goal="Extract relevant metrics and conditions from medical PDFs",
    backstory="An expert healthcare data analyst trained to extract structured clinical insights",
    llm=llm
)