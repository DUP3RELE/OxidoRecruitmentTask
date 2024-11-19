from openai import OpenAI

def generate_article(api_key, article_text):
    client = OpenAI(api_key=api_key)
    
    response = client.chat.completions.create(
        # "gpt-3.5-turbo" = słabsza wersja, mniejsze koszty.
        # "gpt-4o" = mocniejsza wersja, większe koszty.
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Jesteś asystentem, który tworzy fragmenty stron internetowych. Jako "
                                          "odpowiedź wysyłaj tylko i wyłącznie kod, który napisałeś. Zamknij "
                                          "odpowiedź w tagu <body></body>, bez żadnych dodatkowych oznaczeń bloku kodu."},
            {"role": "user",
             "content": f"Stwórz fragment strony HTML, zawarty w tagu <body></body>. Ma to być artykuł, którego treść "
                        f"podana jest tutaj: {article_text}. Wskaż miejsca gdzie warto wstawić grafiki, oznacz je za "
                        f"pomocą tagu <img>, z atrybutem src image_placeholder.jpg. Dodaj atrybut "
                        f"alt zawierający dokładny opis obrazu (prompt do wygenerowania grafiki). Umieść podpisy pod "
                        f"grafikami używając odpowiedniego tagu HTML."}
        ]
    )
    
    response_text = response.choices[0].message.content
    return response_text
