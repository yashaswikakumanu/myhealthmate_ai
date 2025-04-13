from crewai import Agent
from langchain.chat_models import ChatOpenAI

action_recommender_agent = Agent(
    role="Health Strategist",
    goal="Summarize the plan into clear and doable steps",
    backstory="A medical coach who helps users act on insights with urgency and confidence",
    llm=ChatOpenAI(temperature=0.3, model_name="gpt-4o-mini")
)

