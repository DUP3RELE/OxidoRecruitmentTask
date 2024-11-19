from api.get_key import load_api_key
from components.article_loader import load_article
from components.openai_components.openai_body_structure import generate_article
from components.openai_components.openai_html_structure import generate_html_structure
from components.file_saver import save_to_file_article, save_to_file_structure
from components.file_merge import save_to_file_website, merged_html_function

def main():
    # Pobieranie klucza API
    secret_api_key = load_api_key()

    # Ścieżka do artykułu
    article_text_route = './source_files/Zadanie dla JJunior AI Developera - tresc artykulu.txt'

    # Wczytywanie artykułu
    article_text = load_article(article_text_route)

    # Generowanie artykułu
    html_article = generate_article(secret_api_key, article_text)

    # Zapisanie artykułu do pliku
    save_to_file_article(html_article)

    # generowanie struktury
    html_template = generate_html_structure(secret_api_key)

    # zapisanie struktury do pliku
    save_to_file_structure(html_template)

    # funkcja łącząca artykuł z szablonem
    merged_html_code = merged_html_function()

    # funkcja która zapisuje połączony kod html jako podglad.html
    # nie używam api openAi w celu ograniczenia kosztów.
    save_to_file_website(merged_html_code)

if __name__ == "__main__":
    main()
