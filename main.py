import json
from openai import OpenAI


# Część kodu odpowiedzialna za pobieranie klucza API,
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# klucz API
secret_api_key = config.get("OPENAI_API_KEY")
print(secret_api_key)


client = OpenAI(
    api_key=secret_api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Opowiedz coś o kotach, jedno zdanie, maksymalnie 10 słów",
        }
    ],
    model="gpt-4o",
)
print(chat_completion)