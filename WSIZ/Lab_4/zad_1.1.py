Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

print("Pierwszy element:", Moja_lista[0])
print("Ostatni element:", Moja_lista[-1])
print("Długość listy:", len(Moja_lista))
print("Największy element:", max(Moja_lista))
print("Najmniejszy element:", min(Moja_lista))
print("Suma elementów:", sum(Moja_lista))
print("Posortowana lista:", sorted(Moja_lista))

Moja_lista.append(6)
print("Dodanie elementu na końcu:", Moja_lista)

dodanie_na_indeksie = Moja_lista.copy()
dodanie_na_indeksie.insert(3, 5)
print("Dodanie elementu na indeksie 3:", dodanie_na_indeksie)

ostatni_pop = Moja_lista.copy()
usuniety_element = ostatni_pop.pop()
print("Usunięty element (pop):", usuniety_element)
print("Lista po pop():", ostatni_pop)

odwrocona_lista = Moja_lista.copy()
odwrocona_lista.reverse()
print("Odwrotna lista:", odwrocona_lista)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print("Połączona lista:", lista1 + lista2)
print("Powtórzona lista:", lista1 * 5)

print("Wycinek 1 (do indeksu 5):", Moja_lista[:5])
print("Wycinek 2 (od indeksu 4):", Moja_lista[4:])
print("Wycinek 3 (od 2 do 8, krok 2):", Moja_lista[2:8:2])
print("Odwrocona lista (pełne odwrócenie):", Moja_lista[::-1])
