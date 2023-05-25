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
- 0x014 - Nem található a felhasználó, felhasználó be van jelentkezve
- 0x015 - Nem található a felhasználó, felhasználó nincs bejelentkezve
- 0x016 - A kívánt email cím már használatban van! Nem történt változtatás. (Profil adatmódosítás)
- 0x017 - Nem változtattál meg semmit! (Profil adatmódosítás)
- 0x018 - A két új jelszó nem egyezik meg! (Profil adatmódosítás)
- 0x019 - A régi jelszó nem egyezik meg a megadottal! Nem történt változtatás. (Profil adatmódosítás)
- 0x020 - Hiba történt a törlés alatt! (Quiz Pakli)
- 0x021 - Hiba történt a publikussá tétel alatt! (Quiz Pakli)
- 0x022 - Hiba történt a priváttá tétel alatt! (Quiz Pakli)
- 0x023 - Hiba történt a keresésben való megjelenítés alatt! (Quiz Pakli)
- 0x024 - Hiba történt a keresésben való elrejtés alatt! (Quiz Pakli)
- 0x025 - Quiz szerkesztéséhez jelentkezz be vagy regisztrálj!
- 0x026 - Quiz nem található vagy nincs jogod a quiz szereksztéséhez!

## Leírások
- Főoldal: A QuizR egy webes alkalmazás, amely lehetővé teszi a felhasználók számára, hogy saját kvíz paklikat készítsenek, és azokat megosszák másokkal. A QuizR egyben lehetőséget biztosít a felhasználók számára, hogy mások által készített kvíz paklikat tanuljanak, és teszteljék tudásukat.
- Regisztráció: A regisztrációhoz meg kell adni egy felhasználónevet, email címet, jelszót, nemet és születési dátumot. A regisztrációhoz még el kell fogadni az adatkezelési tájékoztató ismeretét. A regisztráció sikeres befejezése után a felhasználó ha bejelölte automatikusan be lesz jelentkezve.
- Bejelentkezés: QuizR bejelentkezési felülete. A bejelentkezéshez meg kell adni az email címet és a jelszót. A bejelentkezés sikeres befejezése után a felhasználó automatikusan be lesz jelentkezve. 
- Adatkezelési tájékoztató: Az adatkezelési tájékoztatóban leírtakat a felhasználóknak el kell fogadniuk a regisztrációhoz. Az adatkezelési tájékoztatóban leírtakat a felhasználók bármikor elolvashatják.
- Hogyan csinálj quizt: A Hogyan csinálj quizt oldalon a felhasználók megismerhetik a QuizR használatát. Különböző lehetőségek, funkciók használatát mutatja be. Alapszintű használati útmutató.
- Új quiz pakli létrehozása: A felhasználók új quiz paklikat hozhatnak létre. A quiz pakli létrehozásához meg kell adni a quiz pakli nevét, kategóriáját és a quiz pakli kártyáit. A quiz pakli létrehozása után a felhasználó átkerül a kész quiz pakli oldalrára.
- Quiz: Tanuld meg a kártyákat könnyebben. Nézd meg a megoldásokat, ha mégsem sikerülne. Majd próbáld meg ismét. A QuizR segít a tanulásban.
- Profil: Itt megtekinthető a saját illetve más felhasználók profiljai. A saját profil esetén adatmódosításra is van lehetőség. Más profilnál pedig a nyilvános quiz paklikat lehet megtekinteni.
- Keresés: A keresés funkció segítségével a felhasználók megkereshetik a quiz paklikat. A kereséshez meg kell adni a keresendő szöveget és a keresés kategóriáját. A keresés lehet a quiz pakli neve vagy a quiz pakli kategóriája. A keresés eredménye a keresési feltételeknek megfelelő quiz paklik listája.
- Quiz pakli szerkesztése: Ez az oldal a quiz pakli szerkesztésére szolgál. A quiz pakli módosítását, a létrehozáshoz hasonlóan kell csinálni. A quiz pakli szerkesztése után a felhasználó átkerül a kész quiz pakli oldalára.
- Hiba: Valami hiba történt. A hiba leírása mellett megjelenik a hiba kódja is. A hiba kódját a fejlesztőknek kell elküldeniük, hogy javítsák a hibát vagy utánajárjanak a problémának.