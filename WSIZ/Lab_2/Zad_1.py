punkty = float(input("Podaj liczbę zdobytych punktów: "))#Użytkownik podaje liczbe zdobytych punktów 

if punkty > 80:
    print("Zaliczyłeś egzamin w terminie 0.")

elif punkty >= 50 and punkty <= 80:
    print("Możesz poprawić wynik egzaminu.")

else:
    print("Musisz poprawić egzamin.")
