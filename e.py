import base64
import requests

# Твой ключ, закодированный в Base64
ENCODED_KEY = "c2stb3ItdjEtYzc2YzI4ZjFkZmYwNzkyMWQxNzYyYmNlYzhmZmRmMjAyODQwNTMxNDk4MTU5YmVlMjU3YTNhYzIzMWFiMmNmZQ=="

# Расшифровываем ключ обратно
API_KEY = base64.b64decode(ENCODED_KEY).decode('utf-8')

MODEL = "nvidia/nemotron-3.5-super-vl:free"
URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_ai(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/",
        "X-Title": "Base64 Honeypot"
    }
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        response = requests.post(URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"Ошибка: {e}"

if __name__ == "__main__":
    print("Привет! Я тестовый ИИ-бот на Python. Спроси меня о чем-нибудь.")
    while True:
        user_input = input("Вы: ")
        if user_input.lower() in ['выход', 'exit', 'quit']:
            break
        print(f"ИИ: {ask_ai(user_input)}")
