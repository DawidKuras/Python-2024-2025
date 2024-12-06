import math
def pole_trojkata(a, b, c):
    try:
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Boki muszą być liczbami dodatnimi")
        
        # Obliczanie półobwodu
        s = (a + b + c) / 2
        
        #warunek trójkąta
        if s <= a or s <= b or s <= c:
            raise ValueError("Podane boki nie tworzą trójkąta")

        # Obliczanie pola trójkąta za pomocą wzoru Herona
        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return pole
    
    except ValueError as ve:
        return f"Błąd: {ve}"
    except Exception as e:
        return f"Wystąpił nieoczekiwany błąd: {e}"

try:
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    c = float(input("Podaj bok c: "))
    wynik = pole_trojkata(a, b, c)
    print(f"Pole trójkąta wynosi: {wynik}")
except ValueError:
    print("Wprowadź poprawne liczby dla boków trójkąta")
