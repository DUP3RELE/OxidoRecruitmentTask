import os

def save_to_file(content, folder_path="../generated_files/", file_name="artykul.html"):
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file_name)
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Plik zapisany w: {file_path}")
