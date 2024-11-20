paliwo = 100
paliwo_zużyte_na_s = 10
czas = 0

paliwo = 100
paliwo_zuzyte_na_s = 10
czas_lotu = 0


while paliwo > 0:
    print(f"Czas: {czas_lotu} s, Pozostałe paliwo: {paliwo} litrów")
    paliwo -= paliwo_zuzyte_na_s
    czas_lotu += 1

print("Koniec lotu.")
