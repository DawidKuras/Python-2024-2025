liczba_gosci = int(input("Podaj liczbę gości: "))
liczba_potraw = int(input("Podaj liczbę zamówionych dań: "))


if liczba_gosci <= 0 or liczba_potraw <= 0:
    print("Liczba gości i liczba potraw muszą być większe od zera.")
else:
    suma_cen = 0
    i = 0


    while i < liczba_potraw:
        cena = float(input(f"Podaj cenę potrawy {i + 1}: "))
        suma_cen += cena
        i += 1


    srednia_cena = suma_cen / liczba_potraw

    rachunek_na_osobe = suma_cen / liczba_gosci

    print(f"\nŚrednia cena potrawy: {srednia_cena:.2f} zł")
    print(f"Rachunek na osobę: {rachunek_na_osobe:.2f} zł")