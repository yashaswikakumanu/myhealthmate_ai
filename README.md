# HealthMate AI — Your Personal AI Health Companion

HealthMate AI is an agentic AI system that analyzes your uploaded medical records and instantly provides:

- Medical Summary & Analysis
- Personalized Meal Plan
- Custom Workout Recommendations
- Health Warnings & Immediate Steps
- Actionable Next Steps & Wellness Plan

Built using **CrewAI**, **LangChain**, and **OpenAI GPT**, HealthMate is not just a chatbot — it's a full-fledged AI agent system powered by **RAG (Retrieval-Augmented Generation)** for accurate, evidence-based health suggestions.

## Live Demo
[Launch Public Dashboard](https://healthmate-ai.streamlit.app)  
*(Replace this with your actual Streamlit link after deployment)*

---

## Architecture

- **PDF Uploader** → Parses your medical report
- **Agent Orchestration** via `CrewAI`:
  - `DiagnosisAgent`: Summarizes your condition
  - `MealPlanAgent`: Suggests meals based on condition
  - `WorkoutAgent`: Gives exercise tips
  - `ImmediateCareAgent`: Lists urgent steps to follow
  - `NextStepsAgent`: Gives long-term guidance
- **RAG Pipeline**:
  - Vector DB: FAISS
  - Embeddings: OpenAI
  - Query Engine: LangChain Retriever
- **Frontend**: Streamlit UI with a sleek, clean dashboard

---

## Tech Stack

| Component           | Tech                      |
|--------------------|---------------------------|
| LLM                | OpenAI GPT-4              |
| Agents             | CrewAI                    |
| RAG                | LangChain + FAISS         |
| Frontend UI        | Streamlit                 |
| PDF Parsing        | PyPDF2                    |
| Deployment         | Streamlit Community Cloud |

