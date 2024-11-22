from langchain_openai.chat_models import ChatOpenAI

import os

# Configurer la clé API OpenAI (ou Ollama)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def chat_without_rag(prompt, temperature=0.7):
    llm = ChatOpenAI(temperature=temperature)
    


    response = llm(prompt)
    return response

if __name__ == "__main__":
    question = input("Posez une question : ")
    response = chat_without_rag(question)
    print(f"Réponse (sans RAG) : {response}")
