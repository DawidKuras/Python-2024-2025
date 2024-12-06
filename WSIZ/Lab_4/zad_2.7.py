def potega(a, n):
    
    if n == 0:
        return 1
    
    elif n < 0:
        return 1 / potega(a, -n)
    
    else:
        return a * potega(a, n - 1)

try:
    a = float(input("Podaj liczbę (a): "))
    n = int(input("Podaj wykładnik (n): "))
    wynik = potega(a, n)
    print(f"{a} do potęgi {n} wynosi: {wynik}")
except ValueError:
    print("Wprowadź poprawne dane (liczba i wykładnik).")
