import pandas as pd

# Dane
pracownicy = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Imie': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja': [8000, 4500, 6000, 5500, 7000]
})

# a) Wybór pracowników z pensją > 5000 PLN
wysoka_pensja = pracownicy[pracownicy['Pensja'] > 5000]
print("Pracownicy z pensją > 5000 PLN:\n", wysoka_pensja)

# b) Sortowanie pracowników według wieku
sortowani_wg_wieku = pracownicy.sort_values(by='Wiek')
print("\nPracownicy posortowani według wieku:\n", sortowani_wg_wieku)

# c) Grupowanie według stanowiska i obliczanie średniej pensji
srednia_pensja_stanowisko = pracownicy.groupby('Stanowisko')['Pensja'].mean()
print("\nŚrednia pensja na stanowiskach:\n", srednia_pensja_stanowisko)

# d) Tworzenie nowej ramki danych dla zmiany stanowiska
zmiany_stanowisk = pd.DataFrame({
    'ID': [2, 4],
    'Nowe_Stanowisko': ['Senior Programista', 'Team Leader']
})
zaktualizowani_pracownicy = pd.merge(pracownicy, zmiany_stanowisk, on='ID', how='left')
print("\nPracownicy po zmianie stanowisk:\n", zaktualizowani_pracownicy)

# e) Zapis danych do pliku CSV
plik_csv = "pracownicy.csv"
zaktualizowani_pracownicy.to_csv(plik_csv, index=False)
print(f"\nDane zapisano do pliku: {plik_csv}")

# f) Wczytanie danych z pliku CSV
wczytane_dane = pd.read_csv(plik_csv)
print("\nWczytane dane z pliku CSV:\n", wczytane_dane)