# Funktionen für die einzelnen Menüoptionen importieren
from divisions import run_divisions
from first_task import run_first
from grade_calculator import run_grade_calculator
from personal_data import run_personal_data

# Menüstruktur ausgeben
print("Menu:")
print("1. Hallo FIA401")
print("2. Notendurchschnittsrechner")
print("3. Persönliche Daten")
print("4. Divisionen")
print("5. Beenden")

#  Benutzereingabe erfassen
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
    print("Programm wird beendet...")
    exit()
else:
    print("Ungültige Eingabe!")
    exit()
