import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

TOGETHER_API_KEY = 'ВАШ_API_КЛЮЧ_ЗДЕСЬ'  # вставь сюда свой ключ

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_message = data.get('message', '')

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "prompt": f"[INST] {user_message} [/INST]",
        "max_tokens": 200,
        "temperature": 0.7,
        "top_p": 0.95
    }

    response = requests.post("https://api.together.xyz/inference", json=payload, headers=headers)

    if response.ok:
        reply = response.json()['output']['choices'][0]['text'].strip()
    else:
        reply = "Извините, произошла ошибка при обращении к модели."

    return jsonify({"message": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
