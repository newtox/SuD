"""
Programm zur Erfassung persönlicher Daten
Sammelt und zeigt persönliche Informationen in strukturierter Form
"""

def main():
    """
    Erfasst persönliche Daten vom Benutzer und
    stellt diese anschließend übersichtlich dar
    """
    # Benutzereingaben für persönliche Daten erfassen
    name = input("Geben Sie Ihren Namen ein: ")
    alter = input("Geben Sie Ihr Alter ein: ")
    stadt = input("Geben Sie Ihre Stadt ein: ")
    beruf = input("Geben Sie Ihren Beruf ein: ")
    
    # Formatierte Ausgabe der erfassten Daten
    print("\n=== Persönliche Informationen ===")
    print(f"Name: {name}")
    print(f"Alter: {alter}")
    print(f"Stadt: {stadt}")
    print(f"Beruf: {beruf}")

if __name__ == "__main__":
    main()