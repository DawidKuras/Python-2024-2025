import pandas as pd

# Wczytaj dane
sciezka = "demografia.csv"
try:
    df = pd.read_csv(sciezka, decimal=",", na_values=["NA", "Brak danych", "N/D"])

    # Wykluczenie kolumny "KRAJE" i znalezienie maksymalnego przyrostu
    df_numeric = df.drop(columns=["KRAJE"], errors="ignore")  
    max_value = df_numeric.max().max()  
    max_column = df_numeric.max().idxmax()  
    max_row_index = df_numeric[max_column].idxmax() 

    # Wyświetlenie
    KRAJE_max = df.loc[max_row_index, "KRAJE"]
    print(f"Kraj: {KRAJE_max}")
    print(f"Rok: {max_column}")
    print(f"Największy przyrost: {max_value}")
except Exception as e:
    print(f"Wystąpił błąd: {e}")
