def oblicz_bmi(waga, wzrost):

    bmi = waga / (wzrost ** 2)

    if bmi < 18.5:
        zakres = "niedowaga"
    elif 18.5 <= bmi < 24.9:
        zakres = "pożądana masa ciała"
    elif 25 <= bmi < 29.9:
        zakres = "nadwaga"
    elif 30 <= bmi < 34.9:
        zakres = "otyłość I stopnia"
    elif 35 <= bmi < 39.9:
        zakres = "otyłość II stopnia"
    else:
        zakres = "otyłość III stopnia"

    return bmi, zakres


waga = float(input("Podaj swoją wagę (kg): "))
wzrost = float(input("Podaj swój wzrost (m): "))

bmi, zakres = oblicz_bmi(waga, wzrost)

print(f"Twoje BMI wynosi: {bmi:.2f}")
print(f"Twoja klasyfikacja BMI: {zakres}")
