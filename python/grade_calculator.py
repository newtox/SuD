"""
Notendurchschnittsrechner
Berechnet den Durchschnitt von drei Schulfächern
"""

def main():
    """
    Erfasst Noten für drei Fächer und berechnet den Durchschnitt
    Die Noten müssen zwischen 1 und 6 liegen
    """
    # Variablen initialisieren
    anzahl_faecher = 3
    summe = 0
    
    # Benutzereingaben für die Noten erfassen
    mathematik = int(input("Geben Sie die Mathematiknote ein (1-6): "))
    deutsch = int(input("Geben Sie die Deutschnote ein (1-6): "))
    englisch = int(input("Geben Sie die Englischnote ein (1-6): "))
    
    # Durchschnittsberechnung durchführen
    summe = mathematik + deutsch + englisch
    durchschnitt = summe / anzahl_faecher
    
    # Ergebnis formatiert ausgeben
    print(f"\nIhr Notendurchschnitt beträgt: {durchschnitt:.2f}")

if __name__ == "__main__":
    main()
