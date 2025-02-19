from math_operations import add, div, mod, mul, sub


# Hauptfunktion für den Taschenrechner
def taschenrechner():
    print("Willkommen zum Taschenrechner!")
    
    while True:
        # Benutzer-Eingabe für die Zahlen
        try:
            zahl1 = float(input("Erste Zahl eingeben: "))
            zahl2 = float(input("Zweite Zahl eingeben: "))
        except ValueError:
            print("Bitte gültige Zahlen eingeben!")
            continue

        # Auswahl der Operation
        print("\nVerfügbare Operationen:")
        print("1: Addition (+)")
        print("2: Subtraktion (-)")
        print("3: Multiplikation (*)")
        print("4: Division (/)")
        print("5: Modulo (%)")
        print("6: Beenden")

        # Benutzer wählt Operation
        auswahl = input("\nOperation wählen (1-6): ")

        # Berechnung durchführen
        if auswahl == '1':
            ergebnis = add(zahl1, zahl2)
            print(f"\nErgebnis: {zahl1} + {zahl2} = {ergebnis}")
        elif auswahl == '2':
            ergebnis = sub(zahl1, zahl2)
            print(f"\nErgebnis: {zahl1} - {zahl2} = {ergebnis}")
        elif auswahl == '3':
            ergebnis = mul(zahl1, zahl2)
            print(f"\nErgebnis: {zahl1} * {zahl2} = {ergebnis}")
        elif auswahl == '4':
            # Prüfung auf Division durch Null
            if zahl2 == 0:
                print("\nFehler: Division durch Null nicht möglich!")
                continue
            ergebnis = div(zahl1, zahl2)
            print(f"\nErgebnis: {zahl1} / {zahl2} = {ergebnis}")
        elif auswahl == '5':
            if zahl2 == 0:
                print("\nFehler: Modulo durch Null nicht möglich!")
                continue
            ergebnis = mod(zahl1, zahl2)
            print(f"\nErgebnis: {zahl1} % {zahl2} = {ergebnis}")
        elif auswahl == '6':
            print("\nAuf Wiedersehen!")
            break
        else:
            print("\nUngültige Eingabe! Bitte wählen Sie eine Zahl zwischen 1 und 6.")

        print("\n" + "-"*50 + "\n")

# Programm starten
if __name__ == "__main__":
    taschenrechner()
