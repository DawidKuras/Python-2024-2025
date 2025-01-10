import numpy as np
import matplotlib.pyplot as plt

def wartosc_liczby_bin(x,y):
    z = 7
    k = 0
    while(z >= 0):
        if(liczba_bin[z] == 1):
            k = k + wagi[z]
        z=z-1
    print(k)

wagi=[128, 64, 32, 16, 8, 4, 2, 1]
liczba_bin=[0, 1, 0, 0, 1, 0, 0, 0]
wartosc_liczby_bin(wagi, liczba_bin)