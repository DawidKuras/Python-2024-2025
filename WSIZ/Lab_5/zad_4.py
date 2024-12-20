import random

# Losowanie szczęśliwej liczby
szczesliwa_liczba = random.randint(1, 1000)
print("Twoja szczęśliwa liczba to: ",szczesliwa_liczba)

# Tablica z rocznikami urodzenia w grupie
roczniki = [2003, 2005, 2001, 2006, 2004, 2024]

# Losowanie szczęśliwego rocznika
szczesliwy_rocznik = random.choice(roczniki)
print("Szczęśliwy rocznik to: ",szczesliwy_rocznik)
