import requests

url = "https://api.perplexity.ai/chat/completions"

payload = {
    "model": "mistral-7b-instruct",
    "messages": [
        {
            "role": "system",
            "content": "Be precise and concise."
        },
        {
            "role": "user",
            "content": "What does API stand for in computer programming?"
        }
    ]
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer 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"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
