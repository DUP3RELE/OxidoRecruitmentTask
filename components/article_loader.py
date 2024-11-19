def load_article(article_text_route):
    with open(article_text_route, 'r', encoding='utf-8') as text_file:
        return text_file.read()
