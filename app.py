import streamlit as st
import tempfile
from services.pdf_processor import load_and_split_pdf
from services.qa_engine import build_prompted_chain, answer_with_custom_prompt
from prompts import QUESTION_PROMPTS

st.set_page_config(page_title="Clinical Trial PDF Analyzer", layout="centered")

st.title("🔬 Clinical Trial PDF Analyzer")
st.markdown("Upload a clinical study PDF to extract key study information.")

uploaded_file = st.file_uploader("📄 Upload Clinical Trial PDF", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    with st.spinner("🔍 Processing document..."):
        split_docs = load_and_split_pdf(tmp_path)
        retriever, llm = build_prompted_chain(split_docs)

    st.success("✅ Document processed successfully!")

    for question in QUESTION_PROMPTS.keys():
        with st.spinner(f"Answering: {question}"):
            result = answer_with_custom_prompt(question, retriever, llm)
            answer = result["result"]
            sources = result.get("source_documents", [])

        st.subheader(f"❓ {question}")
        st.markdown(f"**📝 Answer:** {answer}")

        if sources:
            st.markdown("**📚 Cited Sources:**")
            for doc in sources:
                page = doc.metadata.get("page", "Unknown")
                snippet = doc.page_content[:200].replace("\n", " ")
                st.markdown(f"• **Page {page}**: _{snippet}..._")
