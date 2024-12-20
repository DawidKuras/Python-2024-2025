import pandas as pd

try:
    df = pd.read_csv("demografia.csv", decimal=",", na_values=["NA", "Brak danych", "N/D", "."])
    df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")

    indeks_max = df["2022"].idxmax()
    kraj_max = df.loc[indeks_max, "KRAJE"]
    przyrost_max = df.loc[indeks_max, "2022"]

    print(f"Kraj z największym przyrostem ludności w 2022 roku: {kraj_max} ({przyrost_max})")
except Exception as e:
    print(f"Wystąpił błąd: {e}")
