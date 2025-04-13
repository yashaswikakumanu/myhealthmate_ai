from crew_config import get_healthmate_crew
import streamlit as st
import os
import re

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

def run_healthmate(parsed_text: str) -> dict:
    crew = get_healthmate_crew(parsed_text)
    result = crew.kickoff()
    print("res",result)

    task_outputs = []

    # ✅ Try extracting tasks_output from structured result
    if isinstance(result, dict) and "tasks_output" in result:
        task_outputs = result["tasks_output"]
    elif hasattr(result, "tasks_output"):
        task_outputs = result.tasks_output

    if task_outputs:
        agent_output_map = {task.get("agent", ""): task.get("raw", "") for task in task_outputs}
    else:
        agent_output_map = {}

    # 🔍 If empty, try regex fallback for string output
    if not agent_output_map and isinstance(result, str):
        # Pattern: [DEBUG]: [Agent Name] Task output: content
        pattern = r"\[DEBUG\]: \[(.*?)\] Task output:\s*(.*?)(?=\n\[DEBUG\]:|\Z)"
        matches = re.findall(pattern, result, re.DOTALL)

        for agent, output in matches:
            agent_output_map[agent.strip()] = output.strip()

    return {
        "🩺 Diagnosis Summary": agent_output_map.get("Clinical Diagnosis Specialist", "❌ No diagnosis found."),
        "🥗 Meal Plan": agent_output_map.get("Nutrition Advisor", "❌ No meal plan found."),
        "💪 Workout Plan": agent_output_map.get("Fitness Coach", "❌ No workout plan found."),
        "🚨 Urgent Care": agent_output_map.get("Health Strategist", "❌ No urgent recommendations found."),
        "📅 Next Steps": agent_output_map.get("Health Strategist", "❌ No next steps found."),
    }



# from crew_config import get_healthmate_crew
# import streamlit as st
# import os

# # ✅ Securely use OpenAI key from Streamlit secrets
# os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# def run_healthmate(parsed_text: str) -> dict:
#     crew = get_healthmate_crew(parsed_text)
#     result = crew.kickoff()

#     # Ensure result is a dictionary or convert it safely
#     if hasattr(result, "dict"):
#         result = result.dict()

#     print("res",result)

#     task_outputs = result.get("tasks_output", [])

#     # Map agents to their output
#     agent_output_map = {task["agent"]: task["raw"] for task in task_outputs if task.get("raw")}

#     return {
#         "🩺 Diagnosis Summary": agent_output_map.get("Clinical Diagnosis Specialist", "❌ No diagnosis found."),
#         "🥗 Meal Plan": agent_output_map.get("Nutrition Advisor", "❌ No meal plan found."),
#         "💪 Workout Plan": agent_output_map.get("Fitness Coach", "❌ No workout plan found."),
#         "🚨 Urgent Care": agent_output_map.get("Health Strategist", "❌ No urgent recommendations found."),
#         "📅 Next Steps": agent_output_map.get("Health Strategist", "❌ No next steps found."),
#     }
