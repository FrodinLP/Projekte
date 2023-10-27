# Diese Funktion gibt ein Zahlen-Dreieck aus.

# Schleife für jede Zeile des Dreiecks.
def print_number_triangle(row):
    current_number = 1  # Die aktuelle Zahl, die in jedem Schritt erhöht wird.

    # Schleife für jede Zeile des Dreiecks.
    for i in range(1, row + 1):
        # Schleife für die Zahlen in jeder Zeile.
        for j in range(i):
            # Gib die aktuelle Zahl aus und erhöhe sie.
            print(current_number, end='')
            current_number += 1
        # Füge eine neue Zeile hinzu, um zur nächsten Zeile zu wechseln.
        print()

# Beispielaufruf: Erstelle ein Dreieck mit 4 Zeilen.
print_number_triangle(4)
