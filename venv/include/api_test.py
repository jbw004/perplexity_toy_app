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
    "authorization": "[API KEY]"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)