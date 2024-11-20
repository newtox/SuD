"""
Programm zur Erfassung persönlicher Daten
Dieses Programm sammelt und zeigt persönliche Informationen in strukturierter Form
"""

# Benutzereingaben erfassen
name = input("Geben Sie Ihren Namen ein: ")
alter = input("Geben Sie Ihr Alter ein: ")
stadt = input("Geben Sie Ihre Stadt ein: ")
beruf = input("Geben Sie Ihren Beruf ein: ")

# Gesammelte Informationen strukturiert anzeigen
print("\n=== Persönliche Informationen ===")
print(f"Name: {name}")
print(f"Alter: {alter}")
print(f"Stadt: {stadt}")
print(f"Beruf: {beruf}")
