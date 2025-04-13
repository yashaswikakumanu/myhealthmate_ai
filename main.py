from crew_config import get_healthmate_crew
import streamlit as st
import os

# ✅ Securely use OpenAI key from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

def run_healthmate(parsed_text: str) -> dict:
    crew = get_healthmate_crew(parsed_text)
    result = crew.kickoff()

    # Ensure result is a dictionary or convert it safely
    if hasattr(result, "dict"):
        result = result.dict()

    print("res",result)

    task_outputs = result.get("tasks_output", [])

    # Map agents to their output
    agent_output_map = {task["agent"]: task["raw"] for task in task_outputs if task.get("raw")}

    return {
        "🩺 Diagnosis Summary": agent_output_map.get("Clinical Diagnosis Specialist", "❌ No diagnosis found."),
        "🥗 Meal Plan": agent_output_map.get("Nutrition Advisor", "❌ No meal plan found."),
        "💪 Workout Plan": agent_output_map.get("Fitness Coach", "❌ No workout plan found."),
        "🚨 Urgent Care": agent_output_map.get("Health Strategist", "❌ No urgent recommendations found."),
        "📅 Next Steps": agent_output_map.get("Health Strategist", "❌ No next steps found."),
    }
