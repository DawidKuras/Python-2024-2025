import numpy as np

import matplotlib.pyplot as plt

kategorie = ['żywność', 'obuwie', 'meble', 'posiadłości']

udzial = [100, 20, 15, 2]

plt.pie(udzial, labels=kategorie,

autopct='%1.f%%', startangle=90,
colors=['skyblue', 'lightgreen', 'lightcoral', 'gold'])

plt.title('Udział w kategoriach')
plt.show()