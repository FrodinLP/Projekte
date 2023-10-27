# Überprüfen, ob zwei Werte in einem Wertigkeitsbereich liegen

# Werte von x und y bestimmen
x = 50
y = 15

# Funktion überprüft, ob die Werte x und y in einem gültigen Bereich liegen
def is_valid_range(x, y):
    if 0 < x < 100 and 10 < y < 20:  # Prüfe, ob x zwischen 0 und 100 und y zwischen 10 und 20 liegt
        print("gültiger Bereich")  # Wenn Bedingung erfüllt ist, gebe "gültiger Bereich" aus
    else: print("ungültiger Bereich") # Wenn Bedingung nicht erfüllt ist, gebe "ungültiger Bereich" aus

# Funktion abrufen
is_valid_range(x, y)