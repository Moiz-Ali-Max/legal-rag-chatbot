from rag_pipeline import answer_query, retreive_docs, llm_model
import streamlit as st

st.set_page_config(
    page_title="LegalEase AI - Ask Questions from Legal PDF",
    page_icon="⚖️",
    layout="centered"
)

# --- Title and Intro ---
st.title("⚖️ LegalEase AI: Understand Your Legal Rights Easily")
st.markdown(
    """
    Welcome to **LegalEase AI** — your personal legal assistant powered by AI.
    
    📄 **Step 1**: Upload any legal PDF (e.g., constitution, contract, policy).  
    💬 **Step 2**: Ask questions in plain English or Urdu.  
    🤖 **Step 3**: Get context-aware, trustworthy answers backed by your uploaded document.

    ---
    """
)

# --- File Upload ---
uploaded_file = st.file_uploader("📎 Upload a Legal PDF File", type="pdf", accept_multiple_files=False)
st.divider()

# --- User Question Input ---
user_question = st.text_area(
    "🔍 Ask a question about the uploaded PDF:",
    height=150,
    placeholder="e.g. What rights are violated if peaceful protest is banned?"
)

ask_question = st.button("🤖 Ask AI Lawyer")

# --- RAG Pipeline Execution ---
if ask_question:
    if uploaded_file:
        st.chat_message("user").write(user_question)

        # RAG Pipeline
        retrieved_docs = retreive_docs(user_question)
        response = answer_query(documents=retrieved_docs, model=llm_model, query=user_question)

        st.chat_message("AI Lawyer").write(response)
    else:
        st.error("🚫 Please upload a PDF file before asking a question.")
