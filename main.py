from api.get_key import load_api_key
from components.article_loader import load_article
from components.openai_components.openai_body_structure import generate_article
from components.openai_components.openai_html_structure import generate_html_structure
from components.file_saver import save_to_file_article, save_to_file_structure

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
    save_to_file_article(html_article)

    article_structure = generate_html_structure(secret_api_key)

    save_to_file_structure(article_structure)

if __name__ == "__main__":
    main()
