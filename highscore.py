# Dieser Code prüft, ob ein erreichter Highscore ein neuer Highscore ist

def check_highscore(current_score, highscore):
    # Überprüfe, ob der aktuelle Punktestand größer ist als der aktuelle Highscore.
    if current_score > highscore:
        # Wenn ja, handelt es sich um einen neuen Highscore.
        print(f"Herzlichen Glückwunsch! Neuer Highscore: {current_score}")
    else:
        # Wenn nein, handelt es sich nicht um einen neuen Highscore.
        print(f"Leider kein Glück. Aktueller Highscore: {highscore}")

# Neuer Score und Highscore bestimmen
current_score = 65
highscore = 60

# Aufruf der Funktion
check_highscore(current_score, highscore)
