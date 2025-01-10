import numpy as np
import matplotlib.pyplot as plt

macierz= np.zero((3,3))
print("domyślna\n",macierz)

macierz[2,0:3]=1
print("A\n",macierz)

macierz= np.zero((3,3))
macierz[1:3,1]=1
print("B\n",macierz)

macierz= np.zero((3,3))
macierz[1:3,0:3]=1
print("C\n",macierz)

macierz= np.zero((3,3))
macierz[0:2,0]=1
macierz[0:2,2]=1
print("D\n",macierz)

macierz= np.zero((3,3))
macierz[1:3,1:3]=1
print("E\n",macierz)