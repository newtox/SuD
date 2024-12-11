"""
Notendurchschnittsrechner
Dieses Programm berechnet den Durchschnitt der eingegebenen Noten
"""

def run_grade_calculator():
    # Variablen initialisieren
    anzahl_faecher = 3
    summe = 0
    
    # Benutzereingaben erfassen
    mathematik = int(input("Geben Sie die Mathematiknote ein (1-6): "))
    deutsch = int(input("Geben Sie die Deutschnote ein (1-6): "))
    englisch = int(input("Geben Sie die Englischnote ein (1-6): "))
    
    # Berechnung des Durchschnitts
    summe = mathematik + deutsch + englisch
    durchschnitt = summe / anzahl_faecher
    
    # Ausgabe des Durchschnitts
    print(f"\nIhr Notendurchschnitt beträgt: {durchschnitt:.2f}")
