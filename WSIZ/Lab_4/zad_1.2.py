lista_imion = ["Dawid", "Mikołaj", "Cecylia", "Mariusz"]

# a
lista_posortowana = sorted(lista_imion)
print("Lista posortowana alfabetycznie:", lista_posortowana)

# b
lista_imion.append("Ela")
lista_imion.append("Franek")
usuniety = lista_imion.pop()
print("Lista po dodaniu dwóch osób i usunięciu ostatniej:", lista_imion)
print("Usunięta osoba:", usuniety)

# c
lista_imion.insert(2, "Gosia")
print("Lista po dodaniu osoby na pozycji 3:", lista_imion)

# d
lista_imion.reverse()
lista_zdublowana = lista_imion * 2
print("Lista po odwróceniu kolejności:", lista_imion)
print("Zdublowana lista:", lista_zdublowana)
