x = float(input("Podaj pierwszą liczbę (x): "))
y = float(input("Podaj drugą liczbę (y): "))
z = float(input("Podaj trzecią liczbę (z): "))

najmniejsza = x
srodkowa = y
najwieksza = z

if x > y:
    najmniejsza = y
    najwieksza = x
else:
    najmniejsza = x
    najwieksza = y

if najmniejsza > z:
    srodkowa = najmniejsza
    najmniejsza = z

elif najwieksza < z:
    srodkowa = najwieksza
    najwieksza = z
else:
    srodkowa = z

print("Liczby od najmniejszej do największej:", najmniejsza, srodkowa, najwieksza)