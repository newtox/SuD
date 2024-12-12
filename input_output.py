import sys


def read_file(filename):
    """
    Liest den Inhalt einer Textdatei und gibt ihn auf der Konsole aus.
    Parameter:
        filename (str): Der Name der zu lesenden Datei
    """
    # Versuche die Datei zu öffnen und zu lesen
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Dateiinhalt:")
            print(content)
    except IOError:
        print("Die Datei konnte nicht geöffnet werden.")
    except:
        print("Folgender Fehler ist aufgetreten:", sys.exc_info()[0])

def write_file():
    """
    Ermöglicht dem Benutzer Text in eine Datei zu schreiben.
    Der Benutzer gibt sowohl den Dateinamen als auch den Text ein.
    """
    # Benutzer nach Dateinamen und Text fragen
    try:
        filename = input("Gib den Dateinamen ein (z.B. ausgabe.txt): ")
        text = input("Gib deinen Text ein: ")
        
        # Text in die Datei schreiben
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Dein Text wurde in {filename} gespeichert.")
    except IOError:
        print("Konnte nicht in die Datei schreiben.")
    except:
        print("Folgender Fehler ist aufgetreten: ", sys.exc_info()[0])

def copy_file():
    """
    Kopiert den Inhalt einer Datei in eine andere Datei.
    Benutzer gibt Quell- und Zieldatei an.
    """
    # Benutzer nach Quell- und Zieldatei fragen
    try:
        source = input("Gib den Quelldateinamen ein: ")
        destination = input("Gib den Zieldateinamen ein: ")
        
        # Quelldatei einlesen
        with open(source, 'r') as source_file:
            content = source_file.readlines()
            
        # In Zieldatei schreiben
        with open(destination, 'w') as dest_file:
            dest_file.writelines(content)
        print(f"Die Datei wurde von {source} nach {destination} kopiert.")
    except IOError:
        print("Dateioperation fehlgeschlagen.")
    except:
        print("Folgender Fehler ist aufgetreten: ", sys.exc_info()[0])

def main():
    """
    Hauptfunktion des Programms.
    Zeigt ein Menü an und verarbeitet die Benutzereingaben.
    """
    while True:
        # Menü anzeigen
        print("\nDateioperationen Menü:")
        print("1. Datei lesen")
        print("2. In Datei schreiben")
        print("3. Datei kopieren")
        print("4. Beenden")
        
        choice = input("Wähle eine Option (1-4): ")
        
        # Benutzereingabe verarbeiten
        if choice == '1':
            filename = input("Gib den Dateinamen zum Lesen ein: ")
            read_file(filename)
        elif choice == '2':
            write_file()
        elif choice == '3':
            copy_file()
        elif choice == '4':
            print("Tschüss! Bis zum nächsten Mal!")
            break
        else:
            print("Das war keine gültige Eingabe. Versuch es noch einmal!")

if __name__ == "__main__":
    main()
