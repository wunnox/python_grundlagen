###################################################################
#
# Beispiel2:
# Daten von opendata.swiss
# Nur die Daten der Ladestationen in Bern laden
# Link: https://opendata.swiss/de/dataset/ladestationen-fuer-elektroautos
#
###################################################################

#### Lösung: ####
# KI-Prompt
# Erstelle ein Python Script, welches von diesem Link: https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/data/ch.bfe.ladestellen-elektromobilitaet.json 
# nur die Ladestellen in Bern anzeigt. Der Aufbau der JSON-Datei ist wie folgt: 
# {'EVSEData': [{'EVSEDataRecord': [{'Accessibility': 'Free publicly accessible',
#                                   'AccessibilityLocation': 'OnStreet',
#                                   'AdditionalInfo': None,
#                                   'Address': {'City': 'Lostorf',
#                                               .......

import requests
import json
import pprint

def load_and_filter_charging_stations():
    # URL zu den JSON-Daten
    url = 'https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/data/ch.bfe.ladestellen-elektromobilitaet.json'
    
    print("Lade JSON-Daten herunter...")
    
    try:
        # JSON-Daten von URL herunterladen
        response = requests.get(url)
        response.raise_for_status()  # Fehler bei HTTP-Problemen
        
        data = response.json()
        print(f"JSON-Daten erfolgreich geladen!")
        
        # Ladestellen in Bern filtern
        bern_stations = []
        
        # Durch alle EVSEData-Einträge iterieren
        for evse_data in data['EVSEData']:
            for record in evse_data['EVSEDataRecord']:
                # Prüfen ob die Stadt "Bern" ist (case-insensitive)
                city = record.get('Address', {}).get('City', '').lower()
                if 'bern' in city:
                    bern_stations.append(record)
        
        print(f"\nAnzahl Ladestellen in Bern gefunden: {len(bern_stations)}")
        
        # Ergebnisse anzeigen
        if bern_stations:
            print("\n=== LADESTELLEN IN BERN ===")
            for i, station in enumerate(bern_stations, 1):
                print(f"\n--- Station {i} ---")
                print(f"Station ID: {station.get('ChargingStationId', 'N/A')}")
                print(f"Name: {station.get('ChargingStationNames', [{}])[0].get('value', 'N/A') if station.get('ChargingStationNames') else 'N/A'}")
                print(f"Stadt: {station.get('Address', {}).get('City', 'N/A')}")
                print(f"PLZ: {station.get('Address', {}).get('PostalCode', 'N/A')}")
                print(f"Straße: {station.get('Address', {}).get('Street', 'N/A')}")
                print(f"Koordinaten: {station.get('GeoCoordinates', {}).get('Google', 'N/A')}")
                print(f"24h geöffnet: {station.get('IsOpen24Hours', 'N/A')}")
                print(f"Stecker-Typen: {', '.join(station.get('Plugs', ['N/A']))}")
                
                # Ladeleistung anzeigen
                facilities = station.get('ChargingFacilities', [])
                if facilities:
                    powers = [f"{f.get('power', 'N/A')}kW ({f.get('powertype', 'N/A')})" for f in facilities]
                    print(f"Ladeleistung: {', '.join(powers)}")
                else:
                    print("Ladeleistung: N/A")
        else:
            print("Keine Ladestationen in Bern gefunden.")
        
        # Daten auch in eine Datei schreiben
        if bern_stations:
            output_file = 'ladestationen_bern.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(bern_stations, f, ensure_ascii=False, indent=2)
            print(f"\nAlle Ladestationen in Bern wurden in '{output_file}' gespeichert.")
            
            # Auch eine hübsch formatierte Version mit pprint erstellen
            output_file_pretty = 'ladestationen_bern_pretty.txt'
            with open(output_file_pretty, 'w', encoding='utf-8') as f:
                pprint.pprint(bern_stations, stream=f, width=120)
            print(f"Eine formatierte Version wurde in '{output_file_pretty}' gespeichert.")
        
        return bern_stations
        
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Herunterladen der Daten: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Fehler beim Parsen des JSON: {e}")
        return []
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")
        return []

# Script ausführen
if __name__ == "__main__":
    bern_stations = load_and_filter_charging_stations()

