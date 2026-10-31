import os
import requests
import json

# API
API_KEY = "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"
# MODEL
MODEL = "nvidia/nemotron-3.5-super-vl:free"
URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_ai(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/", # Добавил заголовок, чтобы выглядело реалистичнее
        "X-Title": "Honeypot Test" 
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
