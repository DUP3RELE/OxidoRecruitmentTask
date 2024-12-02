from openai import OpenAI, OpenAIError
from components.token_usage_limiter import log_token_usage

def generate_article(api_key, article_text):
    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            # "gpt-3.5-turbo" = słabsza wersja, mniejsze koszty.
            # "gpt-4o" = mocniejsza wersja, większe koszty.
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Jesteś asystentem, który tworzy fragmenty stron internetowych. Jako "
                                              "odpowiedź wysyłaj tylko i wyłącznie kod, który napisałeś. Zamknij "
                                              "odpowiedź w tagu <body></body>. Podaj odpowiedź bez oznaczeń bloku kodu."},
                {"role": "user",
                 "content": f"Stwórz fragment strony HTML, zawarty w tagu <body></body>. Ma to być artykuł, którego treść "
                            f"podana jest tutaj: {article_text}. Wskaż miejsca gdzie warto wstawić grafiki, oznacz je za "
                            f"pomocą tagu <img>, z atrybutem src image_placeholder.jpg. Dodaj atrybut "
                            f"alt zawierający dokładny opis obrazu, opisany w kilku zdaniach, tak aby za jego pomocą "
                            f"wygenerowano wysokiej jakości grafikę (prompt do wygenerowania grafiki). Umieść podpisy "
                            f"pod grafikami używając odpowiedniego tagu HTML."}
            ]
        )

        tokens_used = response.usage.total_tokens
        print(f"Zużyto {tokens_used} tokenów w operacji stworzenia artykułu.")

        log_token_usage(tokens_used)

        response_text = response.choices[0].message.content
        return response_text

# fragment obsługujący błędy związane z OpenAi
    except OpenAIError as e:
        print(f"Błąd podczas komunikacji z OpenAI (artykuł): {str(e)}")
        return f"Wystąpił błąd podczas generowania artykułu: {str(e)}"

# fragment obsługujący wszystkie nieoczekiwane błędy
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd podczas generowania artykułu: {str(e)}")
        return f"Wystąpił nieoczekiwany błąd podczas generowania artykułu: {str(e)}"
