from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import Ollama


from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.chains.qa_with_sources import load_qa_with_sources_chain

from prompts import QUESTION_PROMPTS

def build_prompted_chain(split_docs):
    # Use BioBERT for embedding biomedical documents
    embeddings = HuggingFaceEmbeddings(
        model_name="dmis-lab/biobert-base-cased-v1.1"
    )
    vectorstore = FAISS.from_documents(split_docs, embedding=embeddings)
    retriever = vectorstore.as_retriever(search_type="mmr", k=10)
    
    llm = Ollama(model="llama3")

    # chain = RetrievalQA.from_chain_type(
    #     llm=llm,
    #     retriever=retriever,
    #     return_source_documents=True,
    #     chain_type="stuff"
    # )
    # return chain

    return retriever, llm

def answer_with_custom_prompt(question, retriever, llm):
    prompt_template = QUESTION_PROMPTS.get(question)
    if not prompt_template:
        return {"result": f"No prompt template found for question: {question}", "source_documents": []}

    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join([doc.page_content for doc in docs])
    formatted_prompt = prompt_template.format(context=context)
    
    print("\n---- Retrieved Context ----\n", context)
    print("\n---- Formatted Prompt ----\n", formatted_prompt)

    response = llm.invoke(formatted_prompt)

    return {
        "result": response,
        "source_documents": docs
    }