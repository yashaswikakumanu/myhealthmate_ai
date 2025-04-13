from crewai import Agent
from langchain.chat_models import ChatOpenAI
from rag.retriever import get_relevant_docs

class DiagnosisAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Clinical Diagnosis Specialist",
            goal="Analyze structured medical data and diagnose potential concerns with evidence",
            backstory="A clinical assistant powered by retrieval-augmented intelligence from recent medical journals",
            llm=ChatOpenAI(temperature=0.3, model_name="gpt-4o-mini")
        )

    def run(self, input):
        docs = get_relevant_docs(input)
        context = "\n".join([d.page_content for d in docs])
        return self.llm.predict(f"Based on this medical context: {context}, and user input: {input}, diagnose health concerns.")

diagnosis_agent = DiagnosisAgent()