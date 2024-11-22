from chat_base import chat_without_rag
from chat_with_rag import chat_with_rag, create_index

if __name__ == "__main__":
    # Simuler des documents
    documents = [
        "Document 1 : Le chat GPT est un modèle de langage.",
        "Document 2 : LangChain est une bibliothèque Python pour les LLM.",
    ]
    index = create_index(documents)

    question = input("Posez une question : ")
    
    print("\n--- Sans RAG ---")
    response_no_rag = chat_without_rag(question)
    print(f"Réponse : {response_no_rag}")

    print("\n--- Avec RAG ---")
    response_with_rag = chat_with_rag(question, index)
    print(f"Réponse : {response_with_rag}")
