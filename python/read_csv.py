import gzip
from csv import DictReader
from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

print("Lade Daten...")

# Liste aller Länder-Codes aus den Daten
COUNTRIES = ['AT', 'BE', 'BG', 'CH', 'CZ', 'DE', 'DK', 'EE', 'ES', 'FI', 
            'FR', 'GB', 'GR', 'HR', 'HU', 'IE', 'IT', 'LT', 'LU', 'LV', 
            'NL', 'NO', 'PL', 'PT', 'RO', 'SE', 'SI', 'SK']

# Datenstruktur für alle Messwerte
data = {
    'dates': [],
    'temperatures': {country: [] for country in COUNTRIES},
    'radiation_direct': {country: [] for country in COUNTRIES},
    'radiation_diffuse': {country: [] for country in COUNTRIES}
}

# Einlesen aller Daten aus der .gzip Datei
with gzip.open('weather_data/combined_weather.txt.gz', 'rt') as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        date = datetime.strptime(row['utc_timestamp'], '%Y-%m-%dT%H:%M:%SZ')
        data['dates'].append(date)
        
        for country in COUNTRIES:
            data['temperatures'][country].append(float(row[f'{country}_temperature']))
            data['radiation_direct'][country].append(float(row[f'{country}_radiation_direct_horizontal']))
            data['radiation_diffuse'][country].append(float(row[f'{country}_radiation_diffuse_horizontal']))

print("Erstelle Plots...")

# Größere Figure erstellen für bessere Lesbarkeit
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(16, 20))

# Temperatur-Plot
for country in COUNTRIES:
    ax1.plot(data['dates'], data['temperatures'][country], label=country, linewidth=1)
ax1.set_title('Temperaturen aller Länder', pad=20, fontsize=14)
ax1.set_xlabel('Datum', fontsize=12)
ax1.set_ylabel('Temperatur (°C)', fontsize=12)
ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., ncol=1)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True, alpha=0.3)

# Direkte Strahlungs-Plot
for country in COUNTRIES:
    ax2.plot(data['dates'], data['radiation_direct'][country], label=country, linewidth=1)
ax2.set_title('Direkte Strahlung aller Länder', pad=20, fontsize=14)
ax2.set_xlabel('Datum', fontsize=12)
ax2.set_ylabel('Direkte Strahlung (W/m²)', fontsize=12)
ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., ncol=1)
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax2.tick_params(axis='x', rotation=45)
ax2.grid(True, alpha=0.3)

# Diffuse Strahlungs-Plot
for country in COUNTRIES:
    ax3.plot(data['dates'], data['radiation_diffuse'][country], label=country, linewidth=1)
ax3.set_title('Diffuse Strahlung aller Länder', pad=20, fontsize=14)
ax3.set_xlabel('Datum', fontsize=12)
ax3.set_ylabel('Diffuse Strahlung (W/m²)', fontsize=12)
ax3.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., ncol=1)
ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax3.tick_params(axis='x', rotation=45)
ax3.grid(True, alpha=0.3)

# Mehr Platz für die Legenden
plt.subplots_adjust(right=0.85, hspace=0.3)

print("Anzeigen...")
plt.show()
