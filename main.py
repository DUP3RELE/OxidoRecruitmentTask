from api.get_key import load_api_key
from components.article_loader import load_article
from components.openai_client import generate_article
from components.file_saver import save_to_file

def main():
    # Pobieranie klucza API
    secret_api_key = load_api_key()

    # Ścieżka do artykułu
    article_text_route = './source_files/Zadanie dla JJunior AI Developera - tresc artykulu.txt'

    # Wczytywanie artykułu
    article_text = load_article(article_text_route)

    # Generowanie HTML
    html_article = generate_article(secret_api_key, article_text)

    # Zapisanie artykułu do pliku
    save_to_file(html_article)

if __name__ == "__main__":
    main()
