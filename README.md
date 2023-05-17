# Projekt 4 WebQuiz 2022-23
**Ez egy olyan webplatform ahol szókártyákat hozhatsz létre és tanulhatsz velük.**

## Setup Process
1. Repo letöltése
2. Python telepítése ([3.11.1](https://www.python.org/downloads/release/python-3111/) Utoljára tesztelve)
3. Szükséges Python csomagok telepítése  `pip install -r requirements.txt`

## Futtatás
`flask run -h <ip> -p <port>`
(`flask run -h 127.0.0.1 -p 5004`)

## Hibakódok
- 0x001 - 
- 0x002 - Quiz nem található, felhasználó be van jelentkezve
- 0x003 - Quiz nem található, felhasználó nincs bejelentkezve
- 0x004 - Quiz nem nyilvános, felhasználó be van bejelentkezve
- 0x005 - Quiz nem nyilvános, felhasználó nincs bejelentkezve
- 0x006 - Quiz sikeresen megmutatva, felhasználó be van jelentkezve, figyelmeztetés, hogy mások számára nem megtekinthető
- 0x007 - Kategória azonosító alapján nem található, felhasználó be van jelentkezve
- 0x008 - Kategória azonosító alapján nem található, felhasználó nincs bejelentkezve
- 0x009 - Nem sikerült betölteni a quiz pakli kártyáit, felhasználó be van jelentkezve
- 0x010 - Nem sikerült betölteni a quiz pakli kártyáit, felhasználó nincs bejelentkezve
- 0x011 - Már van ezzel az email címmel regisztrált felhasználó
- 0x012 - Nem létzeik felhasználó ezzel az email címmel, vagy a jelszó nem megfelelő
- 0x013 - Új pakli készítéséhez be kell jelentkezni

## CSS Szabadon használható osztályok formázáshoz
- .quizcard - Quiz kártya 
- .flipbtn - Quiz kártya fordítás gomb 