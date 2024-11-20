"""
Notendurchschnittsrechner
Dieses Programm berechnet den Durchschnitt der eingegebenen Noten
"""

# Variablen initialisieren
anzahl_faecher = 3
summe = 0

# Noten für jedes Fach einlesen
mathematik = int(input("Geben Sie die Mathematiknote ein (1-6): "))
deutsch = int(input("Geben Sie die Deutschnote ein (1-6): "))
englisch = int(input("Geben Sie die Englischnote ein (1-6): "))

# Durchschnitt berechnen
summe = mathematik + deutsch + englisch
durchschnitt = summe / anzahl_faecher

# Ergebnis ausgeben
print(f"\nIhr Notendurchschnitt beträgt: {durchschnitt:.2f}")
