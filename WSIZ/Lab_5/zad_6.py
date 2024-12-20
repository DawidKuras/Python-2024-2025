import time

czas = int(input("Podaj czas w sekundach: "))

# Sekundnik
for sekunda in range(czas, 0, -1):
    print(f"Do konca pozostało: {sekunda} sekund")
    time.sleep(1)
