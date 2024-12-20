from datetime import datetime

# Mapa nazw miesięcy
miesiace = {
    1: "stycznia", 2: "lutego", 3: "marca", 4: "kwietnia", 5: "maja", 6: "czerwca",
    7: "lipca", 8: "sierpnia", 9: "września", 10: "października", 11: "listopada", 12: "grudnia"
}

# Daty ostatnich laboratoriów i kolokwium
od_labow = datetime(2024, 12, 10)
kolokwium = datetime(2025, 1, 19)
dzisiaj = datetime.now()

# Obliczanie różnic dni
dni_od_labow = (dzisiaj - od_labow).days
dni_do_kolokwium = (kolokwium - dzisiaj).days

#wyniki
print(f"Od ostatnich laboratoriów ({od_labow.day} {miesiace[od_labow.month]} {od_labow.year}) upłynęło: {dni_od_labow} dni.")
print(f"Do kolokwium ({kolokwium.day} {miesiace[kolokwium.month]} {kolokwium.year}) pozostało: {dni_do_kolokwium} dni.")

