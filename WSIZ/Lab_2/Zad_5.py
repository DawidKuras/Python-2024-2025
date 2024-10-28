# Odczytanie i wydrukowanie zawartości pliku
with open("notowania_gieldowe.txt", "r") as plik:
    for line in plik:
        print(plik.read())

# Dopisanie nowej linii do pliku
with open("notowania_gieldowe.txt", "a") as plik:
    plik.write("ALR, 113\n")

# Ponowne odczytanie po dopisaniu nowej linii
with open("notowania_gieldowe.txt", "r") as plik:
    print("\nZawartość po dopisaniu nowej spółki:")
    for line in plik:
        print(plik.read())
