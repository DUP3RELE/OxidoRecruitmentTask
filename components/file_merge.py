import os

# funkcja służąca do łączenia artykul.html i szablon.html
def merged_html_function():
    # funkcja służąca do usuwania tagów <body>
    def clean_body_tags(content):
        if content.startswith('<body>'):
            content = content[len('<body>'):]  # Usuwamy <body> na początku
        if content.endswith('</body>'):
            content = content[:-len('</body>')]  # Usuwamy </body> na końcu
        return content

    # Odczytanie pliku z artykułem i czyszczenie tagów <body>
    with open('./generated_files/artykul.html', 'r', encoding='utf-8') as article_file:
        article_file_content = article_file.read()
        article_file_content = clean_body_tags(article_file_content)

    # Odczytanie pliku z zawartością body
    with open('./generated_files/szablon.html', 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()

    # Znalezienie tagów <body> w pełnym pliku HTML
    body_start = template_file_content.find("<body>")
    body_end = template_file_content.find("</body>")

    # sprawdzenie, czy odnalezione zostało body start i body end
    if body_start != -1 and body_end != -1:
        # fragment przed tagiem <body>
        template_body_start = template_file_content[:body_start + len("<body>")]
        # fragment po tagu </body>
        template_body_end = template_file_content[body_end:]
        # łączenie trzech tekstów w jeden
        merged_html_code = template_body_start + article_file_content + template_body_end
    
    return merged_html_code

# zapisanie strony w pliku podglad.html
def save_to_file_website(merged_html_code, folder_path="./generated_files/", file_name="podglad.html"):
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file_name)
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(merged_html_code)
    print(f"Plik zapisany w: {file_path}")