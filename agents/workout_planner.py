from crewai import Agent
from langchain.chat_models import ChatOpenAI

workout_planner_agent = Agent(
    role="Fitness Coach",
    goal="Generate a fitness routine that aligns with the user’s health conditions",
    backstory="A certified fitness expert creating safe and effective workouts",
    llm=ChatOpenAI(temperature=0.4, model_name="gpt-4o-mini")
)