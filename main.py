from crew_config import get_healthmate_crew
import streamlit as st
import os
import re

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

def run_healthmate(parsed_text: str) -> dict:
    crew = get_healthmate_crew(parsed_text)
    result = crew.kickoff()

    task_outputs = []

    # ✅ Try extracting tasks_output from structured result
    if isinstance(result, dict) and "tasks_output" in result:
        task_outputs = result["tasks_output"]
    elif hasattr(result, "tasks_output"):
        task_outputs = result.tasks_output

    # ✅ If we got structured task_outputs
    if task_outputs:
        agent_output_map = {task.get("agent", ""): task.get("raw", "") for task in task_outputs}
        return {
            "🩺 Diagnosis Summary": agent_output_map.get("Clinical Diagnosis Specialist", "❌ No diagnosis found."),
            "🥗 Meal Plan": agent_output_map.get("Nutrition Advisor", "❌ No meal plan found."),
            "💪 Workout Plan": agent_output_map.get("Fitness Coach", "❌ No workout plan found."),
            "🚨 Urgent Care": agent_output_map.get("Health Strategist", "❌ No urgent recommendations found."),
            "📅 Next Steps": agent_output_map.get("Health Strategist", "❌ No next steps found."),
        }

    # 🔍 Otherwise, fallback: result might be a long string — parse it with regex
    elif isinstance(result, str):
        sections = {
            "🩺 Diagnosis Summary": "",
            "🥗 Meal Plan": "",
            "💪 Workout Plan": "",
            "🚨 Urgent Care": "",
            "📅 Next Steps": ""
        }

        # Match using section markers in markdown or agent names
        for section, marker in [
            ("🩺 Diagnosis Summary", r"(Clinical Diagnosis Specialist[\s\S]*?Task output: )(.*?)(\n\n|\Z)"),
            ("🥗 Meal Plan", r"(Nutrition Advisor[\s\S]*?Task output: )(.*?)(\n\n|\Z)"),
            ("💪 Workout Plan", r"(Fitness Coach[\s\S]*?Task output: )(.*?)(\n\n|\Z)"),
            ("🚨 Urgent Care", r"(Health Strategist[\s\S]*?Task output: )(.*?)(\n\n|\Z)"),
            ("📅 Next Steps", r"(Health Strategist[\s\S]*?Task output: )(.*?)(\n\n|\Z)")
        ]:
            match = re.search(marker, result, re.MULTILINE | re.DOTALL)
            if match:
                sections[section] = match.group(2).strip()

        return {k: v if v else f"❌ No output for {k}" for k, v in sections.items()}

    else:
        # Final fallback if completely unstructured
        return {
            "🩺 Diagnosis Summary": str(result),
            "🥗 Meal Plan": "❌",
            "💪 Workout Plan": "❌",
            "🚨 Urgent Care": "❌",
            "📅 Next Steps": "❌",
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
