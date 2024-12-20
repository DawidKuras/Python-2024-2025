import random

print("\nPodaj przedział liczb do losowania:")
min_val = int(input("Podaj dolna granice: "))
max_val = int(input("Podaj gorna granice: "))

krotka = tuple(random.randint(min_val, max_val) for _ in range(10))
print(f"Wylosowana krotka: {krotka}")

# Obliczanie średniej geometrycznej
iloczyn = 1
for liczba in krotka:
    iloczyn *= liczba

srednia_geometryczna = iloczyn ** (1 / len(krotka))
print(f"Srednia geometryczna krotki wynosi: {srednia_geometryczna:.2f}")