
def oblicz_srednia(lista):
    if len(lista) == 0:
        return 0  
    return sum(lista) / len(lista)

liczby = [10, 20, 30, 40, 50]
srednia = oblicz_srednia(liczby)
print(f"Średnia z listy {liczby} to: {srednia}")
