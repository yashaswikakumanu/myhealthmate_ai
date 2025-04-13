import streamlit as st
from PyPDF2 import PdfReader
from main import run_healthmate
import streamlit as st
import os

# ✅ Securely use OpenAI key from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="HealthMate AI", layout="wide")

st.markdown("""
    <style>
    .big-font {
        font-size:25px !important;
        font-weight: 600;
    }
    .title-font {
        font-size:38px !important;
        font-weight: 800;
        color: #2A9D8F;
    }
    .stButton>button {
        background-color: #2A9D8F;
        color: white;
        font-weight: bold;
        padding: 0.5em 1.2em;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title-font'>My HealthMate AI: Your Personalized Health Companion</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload your medical report (PDF)", type="pdf")

if uploaded_file:
    # Save PDF temporarily
    temp_path = f"temp_docs/{uploaded_file.name}"
    os.makedirs("temp_docs", exist_ok=True)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract text from PDF
    pdf_reader = PdfReader(temp_path)
    parsed_text = "\n".join([page.extract_text() or "" for page in pdf_reader.pages])

    st.success("✅ PDF uploaded and parsed. Running analysis...")

    with st.spinner("HealthMate AI agents analyzing your report..."):
        results = run_healthmate(parsed_text)

    st.markdown("---")
    st.markdown("<div class='big-font'>📊 Agentic Analysis Results</div>", unsafe_allow_html=True)

    # Render each agent result
    for section, content in results.items():
        st.markdown(f"**{section}**")
        st.markdown(
            f"<div style='background-color:#f9f9f9;padding:10px;border-radius:10px;'>{content}</div>",
            unsafe_allow_html=True
        )

    st.balloons()
else:
    st.info("Upload a medical PDF report to begin.")
