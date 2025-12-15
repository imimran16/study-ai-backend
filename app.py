from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    subject = data.get("subject")
    question = data.get("question")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"You are a {subject} teacher. Explain step by step in simple Hindi."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return jsonify({
        "answer": response.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
