ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]

for ulica in ulice:
    for numer_bloku in range(1, 6):
        for numer_lokalu in range(1, 11):
            print(f"{ulica} {numer_bloku}/{numer_lokalu}")
