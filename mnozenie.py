import random
import time

print("Tabliczka mnożenia na czas")

start = time.time()   # uruchom stoper
licznik = 0           # licznik poprawnych odpowiedzi
bledy = 0             # licznik błędów

while licznik < 10:
    a = random.randint(0, 10)
    b = random.randint(0, 10)

    dobrze = False
    while not dobrze:   # pytaj o to samo, aż odpowiedź będzie dobra
        odpowiedz = input("Jaki jest wynik " + str(a) + " · " + str(b) + "? ")

        if not odpowiedz.isdigit():
            print("To nie jest liczba całkowita! Spróbuj jeszcze raz.")
            bledy = bledy + 1
        elif int(odpowiedz) == a * b:
            dobrze = True
        else:
            print("Zła odpowiedź! Spróbuj jeszcze raz.")
            bledy = bledy + 1

    licznik = licznik + 1

czas = time.time() - start   # zatrzymaj stoper
kara = bledy * 10            # każdy błąd to +10 sekund
czas_koncowy = czas + kara

print("Wygrana!")
print("Liczba błędów:", bledy)
print("Czas gry:", round(czas, 1), "sekund")
print("Kara za błędy:", kara, "sekund")
print("Czas końcowy:", round(czas_koncowy, 1), "sekund")