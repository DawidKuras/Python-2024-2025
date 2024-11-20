licznik = 0
liczba = 2

while licznik < 10:
    jest_pierwsza = True
    for i in range(2, liczba):
        if liczba % i == 0:
            jest_pierwsza = False
            break
    if jest_pierwsza:
        print(liczba, end=", " if licznik < 9 else "\n")
        licznik += 1
    liczba += 1