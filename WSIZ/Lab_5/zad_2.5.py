import pandas as pd

# Dane studentów
data = {
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25]
}

# Tworzenie DataFrame
df = pd.DataFrame(data)
print("Oryginalna ramka danych:")
print(df)

# a. Wybierz studentów z oceną większą niż 4
print("\nStudenci z oceną > 4:")
print(df[df['Ocena'] > 4])

# b. Posortuj według wieku
print("\nPosortowani według wieku:")
print(df.sort_values('Wiek'))

# c. Oblicz średni wiek dla każdej grupy ocen
print("\nŚredni wiek w każdej grupie ocen:")
print(df.groupby('Ocena')['Wiek'].mean())

# d. Połącz z danymi z poprawy
data_poprawa = {
    'Nr_albumu': [1, 2, 6],
    'Ocena_poprawa': [5.0, 4.0, 3.5]
}
df_poprawa = pd.DataFrame(data_poprawa)

df_combined = pd.merge(df, df_poprawa, on='Nr_albumu', how='left')
print("\nPołączone DataFrame z poprawą:")
print(df_combined)

# e. Zapisz do pliku CSV
df_combined.to_csv('oceny.csv', index=False)

# f. Wczytaj dane z pliku CSV
df_read = pd.read_csv('oceny.csv')
print("\nWczytane dane z pliku CSV:")
print(df_read)

# g. Dodaj nowego studenta
new_student = {'Nr_albumu': 7, 'Imię': 'Piotr', 'Nazwisko': 'Nowakowski', 'Ocena': 3.5, 'Wiek': 26}
df = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)
print("\nDataFrame z nowym studentem:")
print(df)

# h. Znajdź unikalne wartości w kolumnie 'Ocena'
print("\nUnikalne oceny:")
print(df['Ocena'].unique())

# i. Liczba studentów z oceną równą 5
print("\nLiczba studentów z oceną 5:", (df['Ocena'] == 5.0).sum())
