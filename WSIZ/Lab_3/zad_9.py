#Wczytaj imię i wyświetl „Witaj” oraz imię
imie = input("Podaj swoje imię: ")
print(f"Witaj {imie}!")

#Wczytaj wiek i wyświetl „Twój wiek to: ” oraz wiek
wiek = input("Podaj swój wiek: ")
print(f"Twój wiek to: {wiek}")

#Wczytaj imię i nazwisko, wyświetl inicjały
imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
inicjaly = imie[0] + nazwisko[0]
print(f"Twoje inicjały to: {inicjaly}")

#Wczytaj łańcuch i wyświetl go pięć razy
lancuch = input("Podaj jakiś łańcuch znaków: ")
print(lancuch * 5)

#Wczytaj dwa łańcuchy, połącz je w trzecim łańcuchu
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
polaczony = lancuch1 + lancuch2
print(f"Połączony łańcuch: {polaczony}")

#Wczytaj dwa łańcuchy, zapisz pierwszą połowę obu w trzecim łańcuchu
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
polaczony_polowy = lancuch1[:len(lancuch1)//2] + lancuch2[:len(lancuch2)//2]
print(f"Połączona pierwsza połowa: {polaczony_polowy}")
