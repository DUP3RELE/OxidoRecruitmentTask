import json
from openai import OpenAI
import os

# Część kodu odpowiedzialna za pobieranie klucza API,
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# klucz API
secret_api_key = config.get("OPENAI_API_KEY")
print(secret_api_key)

# ścieżka do artykułu
article_text_route = "./ArticlesUnready/Zadanie dla JJunior AI Developera - tresc artykulu.txt"

# część kodu odpowiedzialna za odczyt pliku .txt
with open(article_text_route, 'r', encoding='utf-8') as text_file:
    contents = text_file.read()

article_text = contents


client = OpenAI(
    api_key=secret_api_key,
)

# funkcja odpowiedzialna za połączenie do api OpenAI, wysłanie propmpta i odbieranie odpowiedzi.
def generate_article(article_text):
    response = client.chat.completions.create(
        # "gpt-3.5-turbo" = słabsza wersja, mniejsze koszty.
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Jesteś asystentem, który tworzy fragmenty stron internetowych. Jako "
                                          "odpowiedź wysyłaj tylko i wyłącznie kod, który napisałeś. Zamknij odpowiedź w tagu <body></body>, tak aby mogła być od razu użyta (bez żadnych dodatkowych znaków)"},
            {"role": "user",
             "content": f"Stwórz fragment strony HTML, zawarty w tagu <body></body>. Ma to być artykuł, którego treść "
                        f"podana jest tutaj: {article_text}. Wskaż miejsca gdzie warto wstawić grafiki, oznacz je za "
                        f"pomocą tagu <img>, z atrybutem src image_placeholder.jpg. do każdego obrazka dodaj atrybut "
                        f"alt, z dokładnym promptem, którego możemy użyć do wygenerowania grafiki. Umieść podpisy pod "
                        f"grafikami używając odpowiedniego tagu HTML."}
        ]
    )
    # odbieranie odpowiedzi, konkretnie części content
    response_text = response.choices[0].message.content
    return response_text


# część kodu odpowiedzialna za włączenie funkcji i odebranie contentu odpowiedzi
html_article = generate_article(article_text)
print(html_article)