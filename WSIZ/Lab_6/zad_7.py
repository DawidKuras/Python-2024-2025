import numpy as np
import matplotlib.pyplot as plt

def fun(x):
    k=0
    l=0
    while (k <= 4):
        while (l <= 4):
            if (macierz[k,l] == 1):
                macierz[k,l] = 0
            else:
                macierz[k,l] = 1
            l=l+1
        k=k+1
        l=0


macierz= np.zeros((5,5))

macierz[0,0]=1

macierz[0,4]=1

macierz[4,4]=1

macierz[4,0]=1

print(macierz)
fun(macierz)
print("\n",macierz)
