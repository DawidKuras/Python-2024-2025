# a
imie = input("Podaj swoje imię: ")
print("Witaj", imie)

# b
wiek = input("Podaj swój wiek: ")
print("Twój wiek to:", wiek)

# c
imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
inicjaly = imie[0] + nazwisko[0]
print("Twoje inicjały to:", inicjaly)

# d
lancuch = input("Podaj dowolny łańcuch znaków: ")
print("Twój łańcuch pięć razy:\n" + (lancuch + "\n") * 5)

# e
lancuch1 = input("Podaj pierwszy łańcuch znaków: ")
lancuch2 = input("Podaj drugi łańcuch znaków: ")
polaczone = lancuch1 + lancuch2
print("Połączone łańcuchy:", polaczone)

# f
lancuch1 = input("Podaj pierwszy łańcuch znaków: ")
lancuch2 = input("Podaj drugi łańcuch znaków: ")
polowa1 = lancuch1[:len(lancuch1) // 2]  
polowa2 = lancuch2[len(lancuch2) // 2:]  
polaczony_lancuch = polowa1 + polowa2
print("Połączony łańcuch z połówek:", polaczony_lancuch)
