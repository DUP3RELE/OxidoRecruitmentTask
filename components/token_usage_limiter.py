import json
import os


def log_token_usage(tokens_used, log_file='token_usage.json'):
    try:
        # Sprawdzamy, czy plik istnieje - jeśli nie, inicjalizujemy pusty plik json
        if os.path.exists(log_file):
            with open(log_file, 'r') as file:
                usage_data = json.load(file)
        else:
            usage_data = {"total_tokens": 0}

        # Aktualizacja liczby zużytych tokenów
        usage_data['total_tokens'] += tokens_used

        # Zapis zaktualizowanych danych do pliku
        with open(log_file, 'w') as file:
            json.dump(usage_data, file, indent=4)  # Używamy indentacji dla lepszego formatowania

        # Ostrzeżenie o przekroczeniu limitu tokenów
        if usage_data['total_tokens'] > 10000:
            print("Zużyłeś już ponad 10000 tokenów!")

        return usage_data['total_tokens']

    except json.JSONDecodeError:
        print("Błąd: Plik JSON jest uszkodzony lub niepoprawnie sformatowany.")
        return None

    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania zużycia tokenów: {str(e)}")
        return None
