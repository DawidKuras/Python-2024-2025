def maksymalna_wartosc(*args):
    try:
       
        maksymalna = max(args)
        return maksymalna
    except TypeError:
        print("Błąd: Wartości nie są porównywalne!")
        return None

wynik = maksymalna_wartosc(1, 2, 3, "Ala", 4.5)
print("Maksymalna wartość:", wynik)
