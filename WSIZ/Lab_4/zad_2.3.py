def powitanie(imie="Użytkowniku", jezyk="polski"):
    if jezyk == "polski":
        print(f"Cześć, {imie}")
    elif jezyk == "angielski":
        print(f"Hello, {imie}")
    elif jezyk == "niemiecki":
        print(f"Guten Morgen, {imie}")
    else:
        print(f"Witaj, {imie}")


# Powitanie w języku polskim
powitanie("Dawid", "polski")

# Powitanie w języku angielskim
powitanie("Dawid", "angielski")

# Powitanie w języku niemieckim
powitanie("Dawid", "niemiecki")

# Powitanie z domyślnym językiem
powitanie("Dawid")

# Powitanie z domyślnymi wartościami (domyślne imię i język)
powitanie()
