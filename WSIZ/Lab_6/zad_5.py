import numpy as np
import matplotlib.pyplot as plt
import random
from random import randint

macierz= np.random.randint(0,1000,(5,5))

print(macierz)

print("ogolny max",macierz.max())
print("ogolny min",macierz.min())
print("wiersz 1 max",macierz[0:1,0:4].max())
print("wiersz 2 max",macierz[1:2,0:4].max())
print("wiersz 3 max",macierz[2:3,0:4].max())
print("wiersz 4 max",macierz[3:4,0:4].max())
print("wiersz 5 max",macierz[4:5,0:4].max())

print("kolumna 1 max",macierz[0:5,0:1].max())
print("kolumna 2 max",macierz[0:5,1:2].max())
print("kolumna 3 max",macierz[0:5,2:3].max())
print("kolumna 4 max",macierz[0:5,3:4].max())
print("kolumna 5 max",macierz[0:5,4:5].max())

print("wiersz 1 suma",macierz[0:1,0:4].sum())
print("wiersz 2 suma",macierz[1:2,0:4].sum())
print("wiersz 3 suma",macierz[2:3,0:4].sum())
print("wiersz 4 suma",macierz[3:4,0:4].sum())
print("wiersz 5 suma",macierz[4:5,0:4].sum())