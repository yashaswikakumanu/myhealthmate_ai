from crewai import Agent
from langchain.chat_models import ChatOpenAI

diet_planner_agent = Agent(
    role="Nutrition Advisor",
    goal="Create a balanced and personalized meal plan for the individual",
    backstory="A certified dietician that prepares healthy and condition-specific food plans",
    llm=ChatOpenAI(temperature=0.5, model_name="gpt-4o-mini")
)