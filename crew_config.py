from crewai import Agent, Task, Crew
from agents.medical_parser import medical_parser_agent
from agents.diagnosis_agent import diagnosis_agent
from agents.diet_planner import diet_planner_agent
from agents.workout_planner import workout_planner_agent
from agents.action_recommender import action_recommender_agent

# Define the crew and task pipeline
def get_healthmate_crew(parsed_text: str) -> Crew:
    parse_task = Task(
        description=f"""Parse the uploaded medical report and extract structured insights from {parsed_text}""",
        expected_output="Dictionary of medical metrics and conditions",
        agent=medical_parser_agent,
        input=parsed_text
    )

    diagnosis_task = Task(
        description="Use parsed data to diagnose any issues or red flags",
        expected_output="List of health concerns",
        agent=diagnosis_agent
    )

    diet_task = Task(
        description="Generate a diet plan based on diagnosed conditions",
        expected_output="Meal plan for the week",
        agent=diet_planner_agent
    )

    workout_task = Task(
        description="Generate a workout plan based on diagnosed conditions and fitness level",
        expected_output="Weekly fitness plan",
        agent=workout_planner_agent
    )

    action_task = Task(
        description="Summarize recommendations into actionable steps",
        expected_output="List of immediate steps with reasoning",
        agent=action_recommender_agent
    )

    crew = Crew(
        agents=[
            medical_parser_agent,
            diagnosis_agent,
            diet_planner_agent,
            workout_planner_agent,
            action_recommender_agent
        ],
        tasks=[
            parse_task,
            diagnosis_task,
            diet_task,
            workout_task,
            action_task
        ],
        verbose=True
    )

    return crew
