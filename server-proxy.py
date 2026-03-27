from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "xai-Gsl6SaUaa9UU1563VTbYehs5oIEsFzelafh0eGbuy9zdOeCcROIuFKmrVn6ss8tmLfX9uayddxuEy6lp"
SYSTEM_PROMPT = "Ты - опытная виртуальная медсестра. Специализация: антибиотикорезистентность. Отвечай кратко (макс 3 предложения). Вопрос пациента: "

@app.route("/server-proxy", methods=["POST"])
def proxy():
    data = request.json
    question = data.get("question", "")

    payload = {
        "model": "llama3-7b-chat",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ]
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://api.groq.com/v1/chat/completions", json=payload, headers=headers)
    if response.status_code != 200:
        return jsonify({"answer": "Ошибка API. Проверьте ключ или сервер."})

    result = response.json()
    answer = result.get("choices", [{}])[0].get("message", {}).get("content", "Нет ответа")
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(port=5000)