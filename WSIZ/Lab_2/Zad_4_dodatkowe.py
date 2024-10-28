gol = int(input("Podaj liczbę zdobytych bramek: "))
bonus = int(input("Podaj początkowy bonus: "))

# Obliczanie punktów za bramki
wynik = gol * 10 + bonus

# Dodanie punktów bonusowych
if gol > 10:
    wynik += 15  # 5 punktów za ponad 5 goli + 10 punktów za ponad 10 goli
elif gol > 5:
    wynik += 5   # 5 punktów za ponad 5 goli

print("Całkowity wynik zespołu:", wynik)
