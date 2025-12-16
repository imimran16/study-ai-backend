from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

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
- Reply politely to greetings.
- Maths → step by step
- History → points + explanation
- Science → concept clear
- Hindi/English → very simple language
- Be friendly and conversational (Hinglish).
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

# ✅ CORRECT MAIN CHECK
if name == "__main__":
    app.run(host="0.0.0.0", port=10000)