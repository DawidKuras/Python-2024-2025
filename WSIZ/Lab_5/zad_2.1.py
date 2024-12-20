import pandas as pd

sciezka = "demografia.csv"
try:
    df = pd.read_csv(sciezka, decimal=",", na_values=["NA", "Brak danych", "N/D"])
    print(df)
except FileNotFoundError:
    print(f"Nie znaleziono pliku: {sciezka}")
