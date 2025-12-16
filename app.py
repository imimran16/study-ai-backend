from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask( __name__ )

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")

    system_prompt = """
You are a friendly AI tutor like ChatGPT.

Rules:
- Talk naturally like ChatGPT.
- Answer EVERY type of question.
- If the user greets (hello, hi, kaise ho) → reply politely.
- If the question is Maths → solve step by step.
- If History → explain in points and simple language.
- If Science → explain concept clearly.
- If Hindi/English → explain in very simple language.
- If the user asks something general → answer normally.
- Do NOT restrict to one subject.
- Always be helpful, friendly, and conversational.
- Use simple Hindi + English mix (Hinglish).
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        temperature=0.7
    )

    return jsonify({
        "answer": response.choices[0].message.content
    })

if name == "main":
    app.run(host="0.0.0.0", port=10000)