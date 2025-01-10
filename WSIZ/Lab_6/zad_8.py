import numpy as np
import matplotlib.pyplot as plt
import random

from random import randint
def fun(x):
    k=0
    l=0
    while (k <= 4):
        while (l <= 4):
            if (macierz[k,l] > 20):
                print(k,",",l)
            l=l+1
        k=k+1
        l=0

macierz= np.random.randint(0,1000,(5,5))

print(macierz)
fun(macierz)