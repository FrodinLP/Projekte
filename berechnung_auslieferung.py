# Ein Unternehmen soll 1000 Kisten für einen Großauftrag ausliefern.
# In LKW passen nur 75 Kisten!
# Wie Oft muss der LKW fahren und wieviele Kisten sind in der letzten Lieferung?

# Gesamtanzahl der Kisten und Kapazität des LKWs
gesamt_kisten = 1000
kapazitaet_pro_lkw = 75

# Berechnung, wie oft der LKW fahren muss
# (// für Ganzzahl)
anzahl_fahrten = gesamt_kisten // kapazitaet_pro_lkw +1

# Berechnung, wie viele Kisten in der letzten Lieferung dabei sind
# (% für den Rest)
kisten_in_letzter_lieferung = gesamt_kisten % kapazitaet_pro_lkw

# Ausgabe der Ergebnisse
print("Der LKW muss", anzahl_fahrten, "mal fahren.")
print("In der letzten Lieferung sind", kisten_in_letzter_lieferung, "Kisten dabei.")