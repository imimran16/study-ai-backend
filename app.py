from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# 🧠 Temporary memory
chat_memory = []

@app.route("/ask", methods=["POST"])
def ask():
    global chat_memory

    data = request.get_json()
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"answer": "Kuch poochho to sahi 🙂"})

    system_prompt = """
You are a friendly AI like ChatGPT.
Answer EVERY question (Maths, History, Hindi, English, Science, General).
Talk naturally and politely.
Use simple Hindi + English (Hinglish).
Remember previous messages.
"""

    chat_memory.append({"role": "user", "content": question})
    chat_memory = chat_memory[-10:]

    messages = [
        {"role": "system", "content": system_prompt}
    ] + chat_memory

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7
        )

        ai_answer = response.choices[0].message.content
        chat_memory.append({"role": "assistant", "content": ai_answer})

        return jsonify({"answer": ai_answer})

    except Exception:
        return jsonify({"answer": "Server error, thoda baad try karo"}), 500


# ✅ VERY IMPORTANT LINE (ERROR FIX HERE)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
