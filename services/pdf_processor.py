from langchain.document_loaders import PyMuPDFLoader
from utils.text_utils import split_documents

def load_and_split_pdf(pdf_path: str):
    loader = PyMuPDFLoader(pdf_path)
    raw_docs = loader.load()
    split_docs = split_documents(raw_docs)
    return split_docs
