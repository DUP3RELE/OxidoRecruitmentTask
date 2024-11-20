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
Sklonuj repozytorium na swój komputer, używając poniższej komendy w konsoli (np. za pomocą edytora kodu VSCode lub PyCharm, w terminalu - Powershell, Bash, itp.):
``` github
git init
```
później sklonuj repozytorium za pomocą
``` github
git clone https://github.com/DUP3RELE/OxidoRecruitmentTask.git
```
przejdź do folderu aplikacji
``` bash
cd OxidoRecruitmentTask
```
upewnij się że masz zainstalowaną bibliotekę openai
``` bash
pip install openai
```
### 2. Stwórz lub wklej plik config.json
Aplikacja nie będzie działać bez klucza API. Możesz stworzyć plik `config.json` i dodać swój klucz, lub zmodyfikować kod, aby przyjmował klucz API jako zmienną środowiskową.
### 3. Włącz program `main.py`
**Upewnij się, że masz zainstalowanego Pythona na swoim systemie.** <br>
*Aby uzyskać pełniejszy efekt, usuń wszystkie pliki z folderu `generated_files` przed uruchomieniem programu.* <br>
<br>
Następnie, w głównym folderze aplikacji, uruchom program za pomocą poniższej komendy:
``` bash
python main.py
```
Poczekaj chwilę, generowanie plików może trochę potrwać.
Gotowy kod HTML wygenerowany za pomocą OpenAI API będzie zapisany w folderze *`generated_files`*
### 4. Sprawdzanie gotowego kodu
Podgląd gotowego kodu możesz zobaczyć za pomocą edytora kodu (np. Visual Studio Code) z rozszerzeniem Live Server lub otwierając plik `podglad.html` w domyślnej przeglądarce.

## Użyte technologie
- Github = kontrola wersji, udostępnianie kodu
- PyCharm Community Edition = edycja kodu w Pythonie
- OpenAI API = dostarczanie promptów i odbieranie gotowych komponentów

## Dodatkowe informacje
- Do generacji kodu użyty został model gpt-4. Idealnym modelem byłby davinci-002, jednak zgodnie z dokumentacją OpenAI, jego rozwój został zakończony.
- Kolejnym dobrym rozwiązaniem byłoby stworzenie asystenta OpenAI, jednak postanowiłem jeszcze nie korzystać z tej funkcji, ponieważ jest w fazie beta. W systemie OpenAI można zarejestrować asystenta i przypisać mu, za pomocą instrukcji (instructions), dowolną rolę (np. kreatora kodu, dodając szczegółowe informacje na temat jego zadania). Za pomocą narzędzi (tools), takich jak `{"type": "code_interpreter"}`, można również dodać niezbędne funkcje. Dzięki tak stworzonemu asystentowi moglibyśmy wysyłać jeszcze krótsze prompty i otrzymywać bardziej precyzyjne odpowiedzi.  [Link do dokumentacji asystenta openai (beta)](https://platform.openai.com/docs/api-reference/assistants)
