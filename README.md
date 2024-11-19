# Generator Artykułów z OpenAI, rekrutacja dla Oxido
## Ważne!
 Z powodów bezpieczeństwa nie wysyłam klucza API OpenAI do repozytorium GitHub. Do obsługi kodu niezbędny jest plik `config.json`, który wysłałem na adres e-mail, z którego otrzymałem informację o rekrutacji. Proszę sprawdzić, czy dotarł. Jeśli nie, należy w głównym folderze aplikacji utworzyć plik config.json i umieścić w nim poniższy kod, zamieniając "YOUR_OPENAI_API_KEY" na swój klucz API:
  ```json
    {
	"OPENAI_API_KEY": "YOUR_OPENAI_API_KEY"
}
```
Alternatywnie, możesz zmodyfikować kod, aby przyjmował klucz API jako zmienną środowiskową.
## Opis
Projekt to aplikacja do generowania artykułów i szablonów z wykorzystaniem API OpenAI oraz Pythona. Aplikacja automatyzuje proces tworzenia artykułu i szablonu na podstawie wysyłanych promptów, a następnie za pomocą Pythona łączy wygenerowane kody HTML w gotowy podgląd strony.
## Instrukcja obsługi
### 1. Pobierz repozytorium git na lokalny system:
Sklonuj repozytorium na swój komputer, używając poniższej komendy w konsoli (np. za pomocą edytora kodu VSCode, w terminalu - Powershell, Bash, itp.):
``` github
git init
```
później sklonuj repozytorium za pomocą
``` github
git clone https://github.com/DUP3RELE/OxidoRecruitmentTask.git
```
### 2. Stwórz lub wklej plik config.json
Aplikacja nie będzie działać bez klucza API. Możesz dodać swój klucz do pliku `config.json` lub zmodyfikować kod, aby przyjmował klucz API jako zmienną środowiskową.
### 3. Włącz program `main.py`
**Upewnij się, że masz zainstalowanego Pythona na swoim systemie.** <br>
*Aby uzyskać pełniejszy efekt, usuń wszystkie pliki z folderu `generated_files` przed uruchomieniem programu.* <br>
<br>
Następnie, w głównym folderze aplikacji, uruchom program za pomocą poniższej komendy:
``` bash
python main.py
```
Gotowy kod HTML wygenerowany za pomocą OpenAI API będzie zapisany w folderze *`generated_files`*
### 4. Sprawdzanie gotowego kodu
Podgląd gotowego kodu możesz zobaczyć za pomocą edytora kodu (np. Visual Studio Code) z rozszerzeniem Live Server lub otwierając plik `podglad.html` w domyślnej przeglądarce.

## Użyte technologie
- Github = kontrola wersji, udostępnianie kodu
- PyCharm Community Edition = edycja kodu w Pythonie
- OpenAI API = dostarczanie promptów i odbieranie gotowych komponentów
