zakupy = {
    "Mleko": 3.50,
    "Chleb": 8.00,
    "Masło": 88.00,
    "Tunczyk": 74.00,
    "Jabłka": 34.00
}

print("Lista zakupów:")
for artykul, kwota in zakupy.items():
    print(f"{artykul}: {kwota} zł")

wydatki = sum(zakupy.values())
print(f"\nPodsumowanie wydatków: {wydatki} zł")
