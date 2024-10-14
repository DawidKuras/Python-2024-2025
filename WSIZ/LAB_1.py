#A)

# a=1
# a=a+1
# print(a)
#typ wyniku 1+2
x = 1 + 2
print(type(x))
#<class 'int'>

#typ wyniku 1 + 4.5
x = 1 + 4.5
print(type(x))
#<class 'float'>

#typ wyniku 3/2
x = 3 / 2
print(type(x))
#<class 'float'>

#typ wyniku 4 / 2
x = 4 / 2
print(type(x))
#<class 'float'>

#typ wyniku 3 // 2
x = 3 // 2
print(type(x))
#<class 'int'>

#typ wyniku -3 // 2
x = -3 // 2
print(type(x))
#<class 'int'>

#typ wyniku 11 % 2
x = 11 % 2
print(type(x))
#<class 'int'>

#typ wyniku 2 ** 10
x = 2 ** 10
print(type(x))
#<class 'int'>

#typ wyniku 8 ** (1/3)
x = 8 ** (1/3)
print(type(x))
#<class 'float'>

#B)

#int(3.0)
x = int(3.0)
print(type(x))
#<class 'int'>

#float(3)
x = float(3)
print(type(x))

#float(3)
x = float("3")
print(type(x))

#str(12.4)
x = str(12.4)
print(type(x))

#bool(0)
x = bool(0)
print(type(x))
      
#Powyższe instrukcje konwertują wartosci na zadany typ danych ktore są podane w nawiasie.


#ZAD2

uczelnia = "Studiuje na WSiZ"
print(uczelnia)

#ZAD3

imię = 'Jan'
wiek = 20
wzrost = 178

print(f"Nazywam się {imię} i mam {wiek} lat.")
print(f"Mój wzrost to {wzrost} cm.")


# #ZAD4
# Cena = 39.99
# Rabat = 0.2

# Cena_po_rabacie = Cena * (1 - Rabat)

# print(f"Cena produktu po rabacie wynosi: {Cena_po_rabacie:.2f} PLN")



# #ZAD5

# a = float(input("Podaj pierwszy bok prostokąta: "))
# print(a)

# b = float(input("Podaj drugi bok prostokata: "))
# print(b)

# pole = a * b
# obwod = 2 * a + 2 * b

# print("pole prostokata: ", pole)
# print("obowd prostokata: ", obwod)


#ZAD6
#s = int(input("podaj dlugosc drogi: "))
import random
s = random.randint(1, 1000)
print(f"wylosowana odleglosc{s}")

spalanie = float(input("Podaj srednie spalanie w litrach na 100km: "))
print(spalanie)

zuzycie = s / spalanie
koszt = zuzycie * 6.5

print("spalone paliwo", zuzycie)
print("koszt przejechanej drogi: ", koszt)