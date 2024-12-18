from openai import OpenAI, OpenAIError
from components.token_usage_limiter import log_token_usage


def generate_html_structure(api_key):
    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            # "gpt-3.5-turbo" = słabsza wersja, mniejsze koszty.
            # "gpt-4o" = mocniejsza wersja, większe koszty.
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Jesteś asystentem, który tworzy fragmenty stron internetowych. Jako "
                                              "odpowiedź wysyłaj tylko i wyłącznie kod, który napisałeś. Zamknij "
                                              "odpowiedź w tagu <HTML></HTML>. Podaj odpowiedź bez oznaczeń bloku kodu."},
                {"role": "user",
                 "content": "Stwórz responsywny szablon strony www napisany w HTML, używany do wyświetlania gotowych "
                            "artykułów. Artykuły mają być wyświetlane na 90% szerokości ekranu. Dodaj proste style CSS i "
                            "kod JS, który umożliwi dynamiczną zmianę między trybem jasnym i ciemnym, w zależności od "
                            "ustawień systemu użytkownika. Sekcja <body> powinna być pusta i gotowa na wklejenie artykułu."
                            "Stosuj style bezpośrednio do elementów HTML, bez użycia klas. artykuł jest zamknięty w tagu "
                            "<body>, który zawiera tagi <article> (tag w którym znajduje się cały artykuł), <h1>, "
                            "<section>, <h2>, <p>, <img>, <figcaption>, <footer>. Dla JS dodaj funkcję która pilnuje "
                            "trybu jasnego lub ciemnego - zależnie od tego jaki tryb ma ustawiony użytkownik, dostosuj "
                            "style CSS. dodaj do <script> atrybut defer, umieść <script> w tagu <head>. Podaj odpowiedź bez oznaczeń bloku kodu"
                            }
            ]
        )

        tokens_used = response.usage.total_tokens
        print(f"Zużyto {tokens_used} tokenów w operacji stworzenia struktury html.")

        log_token_usage(tokens_used)

        response_structure = response.choices[0].message.content
        return response_structure

    except OpenAIError as e:
        print(f"Błąd podczas komunikacji z OpenAI (struktura html): {str(e)}")
        return f"Wystąpił błąd podczas generowania struktury html: {str(e)}"

    # fragment obsługujący wszystkie nieoczekiwane błędy
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd podczas generowania struktury html: {str(e)}")
        return f"Wystąpił nieoczekiwany błąd podczas generowania struktury html: {str(e)}"