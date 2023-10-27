# Überprüfen, ob zwei Werte in einem Wertigkeitsbereich liegen

# Werte von x und y bestimmen
x = 50
y = 15

# Funktion überprüft, ob die Werte x und y in einem gültigen Bereich liegen
def is_valid_range(x, y):
    if 0 < x < 100 and 10 < y < 20:  # Prüfe, ob x zwischen 0 und 100 und y zwischen 10 und 20 liegt.
        print("VALID RANGE")  # Wenn die Bedingung erfüllt ist, gebe "VALID RANGE" aus.
    else: print("UNVALID RANGE")

# Funktion abrufen
is_valid_range(x, y)