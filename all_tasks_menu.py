"""
Hauptmenü-Programm
Stellt ein Auswahlmenü für verschiedene Programmfunktionen bereit
"""

# Funktionen für die einzelnen Menüoptionen importieren
from divisions import main as run_divisions
from first_task import main as run_first
from grade_calculator import main as run_grade_calculator
from input_output import main as run_input_output
from personal_data import main as run_personal_data


def main():
    """
    Hauptfunktion zum Anzeigen und Verarbeiten des Menüs
    """
    # Menüstruktur ausgeben
    print("Menu:")
    print("1. Hallo FIA401")
    print("2. Notendurchschnittsrechner")
    print("3. Persönliche Daten")
    print("4. Divisionen")
    print("5. Input/Output")
    print("6. Beenden")

    # Benutzereingabe erfassen und verarbeiten
    choice = input("Bitte wählen Sie eine Option (1-5): ")

    # Auswahl des Menüpunkts und Aufruf der entsprechenden Funktion
    if choice == "1":
        run_first()
    elif choice == "2":
        run_grade_calculator()
    elif choice == "3":
        run_personal_data()
    elif choice == "4":
        run_divisions()
    elif choice == "5":
        run_input_output()
    elif choice == "6":
        print("Programm wird beendet...")
        exit()
    else:
        print("Ungültige Eingabe!")
        exit()

if __name__ == "__main__":
    main()
