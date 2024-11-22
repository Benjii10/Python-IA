from langchain_openai.chat_models import ChatOpenAI

from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

from langchain.chains import RetrievalQA
import os

# Configurer les clés
os.environ["OPENAI_API_KEY"] = "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"

# Initialiser les embeddings et FAISS
def create_index(documents):
    embeddings = OpenAIEmbeddings()
    index = FAISS.from_texts(documents, embeddings)
    return index

def chat_with_rag(question, index, temperature=0.7):
    retriever = index.as_retriever()
    qa = RetrievalQA(llm=ChatOpenAI(temperature=temperature), retriever=retriever)

    return qa.run(question)

if __name__ == "__main__":
    # Simuler des documents récupérés
    documents = [
        "Document 1 : Le chat GPT est un modèle de langage.",
        "Document 2 : LangChain est une bibliothèque Python pour les LLM.",
    ]
    index = create_index(documents)

    question = input("Posez une question : ")
    response = chat_with_rag(question, index)
    print(f"Réponse (avec RAG) : {response}")

temperature = float(input("Choisissez une température (0.0 à 1.0) : "))
response_with_rag = chat_with_rag(question, index, temperature=temperature)
print(f"Réponse (avec température ajustée) : {response_with_rag}")
