# Definiowanie krotki stopnie
stopnie = (
    "Szeregowy",
    "Kapral",
    "Sierżant",
    "Porucznik",
    "Kapitan",
    "Major",
    "Pułkownik",
)


ilość_stopnii = len(stopnie)


Major_index = stopnie.index("Major")


Pułkownik_krotka = "Pułkownik" in stopnie


print("Liczba stopni wojskowych:", ilość_stopnii)
print("Indeks stopnia Major:", Major_index)
print("Czy 'Pułkownik' znajduje się w krotce?", Pułkownik_krotka)
