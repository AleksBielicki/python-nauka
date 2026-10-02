"""Czarodziej Kodu - gra do nauki Pythona dla ucznia 3 klasy.

Uruchomienie:  python3 czarodziej_kodu.py
Dziecko pomaga czarodziejowi otworzyć magiczne drzwi, poznając
print, zmienne, pętlę for oraz if/else.
"""

import io
import contextlib

gwiazdki = 0


def pokaz_kod(kod):
    """Wyświetla kod w ramce, żeby dziecko widziało go wyraźnie."""
    print("\n  ┌─── KOD ───────────────")
    for linia in kod.strip().splitlines():
        print("  │ " + linia)
    print("  └───────────────────────")


def uruchom_kod(kod):
    """Wykonuje kod i zwraca to, co wypisał (żeby pokazać magię na żywo)."""
    bufor = io.StringIO()
    with contextlib.redirect_stdout(bufor):
        exec(kod, {})
    return bufor.getvalue().strip()


def zapytaj(pytanie, poprawne, podpowiedz):
    """Pyta o odpowiedź; dziecko ma 3 próby, za każdą porażką dostaje wskazówkę."""
    global gwiazdki
    for proba in range(3):
        odp = input(pytanie + " ").strip().lower()
        if odp in [p.lower() for p in poprawne]:
            gwiazdki += 1
            print("⭐ Brawo! Dostajesz gwiazdkę! (razem: %d)" % gwiazdki)
            return True
        print("🤔 Prawie! Podpowiedź:", podpowiedz)
    print("Nic nie szkodzi, poprawna odpowiedź to:", poprawne[0])
    return False


def poziom_1():
    print("\n=== POZIOM 1: Zaklęcie print ===")
    print("Czarodziej mówi: 'Komputer powtarza to, co każesz mu print()!'")
    pokaz_kod('print("Abrakadabra!")')
    print("Wynik:", uruchom_kod('print("Abrakadabra!")'))
    print("Teraz Ty! Napisz zaklęcie, które wypisze słowo: Sezamie")
    for _ in range(3):
        wpis = input(">>> ").strip()
        if wpis.replace("'", '"').replace(" ", "") == 'print("Sezamie")':
            global gwiazdki
            gwiazdki += 1
            print("⭐ Drzwi drgnęły! Dostajesz gwiazdkę! (razem: %d)" % gwiazdki)
            print("Wynik:", uruchom_kod(wpis))
            return
        print('🤔 Wpisz dokładnie: print("Sezamie")  (cudzysłów ważny!)')
    print('Poprawnie: print("Sezamie")')


def poziom_2():
    print("\n=== POZIOM 2: Zmienne - magiczne pudełka ===")
    kod = 'smoki = 3\nsmoki = smoki + 2\nprint(smoki)'
    print("Zmienna to pudełko z nazwą, w którym trzymamy wartość.")
    pokaz_kod(kod)
    zapytaj("Ile smoków wypisze komputer?", ["5"], "najpierw było 3, potem dodajemy 2")
    print("Sprawdźmy! Komputer wypisał:", uruchom_kod(kod))


def poziom_3():
    print("\n=== POZIOM 3: Pętla for - powtarzanie ===")
    kod = 'for i in range(4):\n    print("Hop!")'
    print("Pętla for powtarza polecenie wiele razy.")
    pokaz_kod(kod)
    zapytaj("Ile razy pojawi się napis Hop!?", ["4", "cztery"], "range(4) znaczy cztery razy")
    print("Zobacz:\n" + uruchom_kod(kod))


def poziom_4():
    print("\n=== POZIOM 4: if / else - podejmowanie decyzji ===")
    kod = ('klucze = 2\n'
           'if klucze >= 3:\n'
           '    print("Drzwi otwarte!")\n'
           'else:\n'
           '    print("Szukaj dalej!")')
    print("if znaczy 'jeśli', else znaczy 'w przeciwnym razie'.")
    pokaz_kod(kod)
    zapytaj("Co wypisze komputer? (otwarte / szukaj)",
            ["szukaj", "szukaj dalej", "szukaj dalej!"],
            "czy 2 jest większe lub równe 3?")
    print("Komputer wypisał:", uruchom_kod(kod))


def koniec():
    print("\n" + "=" * 40)
    print("Zebrane gwiazdki: " + "⭐" * gwiazdki + " (%d/4)" % gwiazdki)
    if gwiazdki == 4:
        print("🚪✨ Magiczne drzwi się otwierają! Jesteś Mistrzem Pythona!")
    elif gwiazdki >= 2:
        print("🚪 Drzwi są uchylone! Zagraj jeszcze raz, by je otworzyć.")
    else:
        print("🚪 Drzwi zamknięte, ale dobrze Ci poszło! Spróbuj ponownie.")


def main():
    print("🧙 Witaj w grze CZARODZIEJ KODU! 🧙")
    imie = input("Jak masz na imię? ").strip() or "Przyjacielu"
    print("Cześć, %s! Pomóż mi otworzyć magiczne drzwi, rozwiązując zagadki Pythona." % imie)
    for poziom in (poziom_1, poziom_2, poziom_3, poziom_4):
        poziom()
        input("\n(naciśnij Enter, aby iść dalej)")
    koniec()


if __name__ == "__main__":
    main()
