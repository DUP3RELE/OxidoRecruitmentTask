from openai import OpenAI

def generate_html_structure(api_key):
    client = OpenAI(api_key=api_key)
    
    response = client.chat.completions.create(
        # "gpt-3.5-turbo" = słabsza wersja, mniejsze koszty.
        # "gpt-4o" = mocniejsza wersja, większe koszty.
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Jesteś asystentem, który tworzy fragmenty stron internetowych. Jako "
                                          "odpowiedź wysyłaj tylko i wyłącznie kod, który napisałeś. Zamknij odpowiedź w tagu <HTML></HTML>, tak aby mogła być od razu użyta (bez żadnych dodatkowych znaków)"},
            {"role": "user",
             "content": f"Stwórz szablon dla strony www, napisany w HTML, zadbaj o to aby był responsywny. Ma on być używany do oglądania gotowych artykułów. Dodaj proste style CSS i kod JS, które pozwolą na wizualizację kodu po wklejeniu jego kodu do sekcji <body>. Sekcja <body> powinna być pusta i gotowa na wklejenie artykułu. style przypisz do tagów, artykuł zawiera tagi <article>, <h1>, <section>, <h2>, <p>, <img>, <figcaption>, <footer>. Dla JS dodaj funkcję która pilnuje trybu jasnego lub ciemnego, zależnie od tego jaki tryb ma ustawiony użytkownik, dostosuj style CSS. dodaj do <script> atrybut defer, umieść <script> w tagu <head>."}
        ]
    )
    
    response_structure = response.choices[0].message.content
    return response_structure
