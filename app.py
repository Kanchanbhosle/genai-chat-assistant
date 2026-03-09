from flask import Flask, render_template, request
import json
import ollama
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)

print("Loading embedding model...")


model = SentenceTransformer("all-MiniLM-L6-v2")

with open("docs.json", "r") as f:
    docs = json.load(f)

texts = [doc["content"] for doc in docs]

doc_embeddings = model.encode(texts)

chat_history = []



def retrieve_context(query, top_k=3):

    query_embedding = model.encode([query])

    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]

    top_indices = np.argsort(similarities)[-top_k:][::-1]

    top_contexts = [texts[i] for i in top_indices]

    combined_context = "\n".join(top_contexts)

    return combined_context


@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":

        question = request.form["question"]

      
        if question.lower() in ["hi", "hello", "hey"]:
            answer = "Hello! How can I assist you today?"

        else:

            context = retrieve_context(question)

            print("Retrieved Context:", context)

            prompt = f"""
You are a helpful AI assistant.

Answer the question ONLY using the information provided in the context.

Context:
{context}

Question:
{question}

Answer:
"""

            response = ollama.chat(
                model="tinyllama",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            answer = response["message"]["content"]

        chat_history.append({
            "q": question,
            "a": answer
        })

    return render_template("index.html", history=chat_history)


if __name__ == "__main__":
    print("Server starting...")
    app.run(debug=True)