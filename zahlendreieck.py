# Diese Funktion gibt ein Zahlen-Dreieck aus.

def print_number_triangle(row):
    # Schleife für jede Zeile des Dreiecks.
    for i in range(1, row + 1):
        # Schleife für die Zahlen in jeder Zeile.
        for j in range(1, i + 1):
            # Gib die aktuelle Zahl aus.
            print(j, end='')
        # Füge eine neue Zeile hinzu, um zur nächsten Zeile zu wechseln.
        print()

# Erstelle ein Dreieck mit 4 Zeilen.
print_number_triangle(4)
