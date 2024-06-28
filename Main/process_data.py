import json
import googlemaps
from datetime import datetime
import time 

# The program should accept a CSV file containing historical rainfall data. Each entry should include a timestamp,
# location (latitude and longitude), and rainfall amount (in mm).
# Process this data to calculate the average rainfall over different regions.

def process_data():
    time.sleep(0.1)  # Simulate some processing time

def parse_date(timestr):
    # parse the date from JSON
    try:
        dt = datetime.strptime(timestr, '%Y-%m-%d %H:%M:%S %z %Z')
        return dt
    except ValueError:
        raise ValueError(f"Unknown string format: {timestr}")
    
data = []

# process the JSON data
with open('data.json', 'r') as f:
    for line in f:
        try:
            data.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

filtered_json = open('filtered_data.json', 'w')

# Define the date range
start_date = parse_date('2024-05-14 00:00:00 +0000 UTC')
end_date = parse_date('2024-05-17 23:59:59 +0000 UTC')

# Cities in Saarland
cities_in_saarland_coords = {
    "Blieskastel": {"latitude": 49.2374, "longitude": 7.2576},
    "Bexbach": {"latitude": 49.3483, "longitude": 7.2557},
    "Dillingen": {"latitude": 49.3561, "longitude": 6.7293},
    "Friedrichsthal": {"latitude": 49.3186, "longitude": 7.0831},
    "Homburg": {"latitude": 49.3231, "longitude": 7.3384},
    "Illingen": {"latitude": 49.3883, "longitude": 7.0484},
    "Lebach": {"latitude": 49.4142, "longitude": 6.9105},
    "Merchweiler": {"latitude": 49.3528, "longitude": 7.0556},
    "Merzig": {"latitude": 49.4439, "longitude": 6.6377},
    "Neunkirchen": {"latitude": 49.3514, "longitude": 7.1839},
    "Ottweiler": {"latitude": 49.4003, "longitude": 7.1684},
    "Püttlingen": {"latitude": 49.2861, "longitude": 6.8975},
    "Saarbrücken": {"latitude": 49.2401, "longitude": 6.9969},
    "Saarlouis": {"latitude": 49.3139, "longitude": 6.7518},
    "Sankt Ingbert": {"latitude": 49.2761, "longitude": 7.1168},
    "Sankt Wendel": {"latitude": 49.4667, "longitude": 7.1689},
    "Schiffweiler": {"latitude": 49.3772, "longitude": 7.1267},
    "Völklingen": {"latitude": 49.2528, "longitude": 6.8617},
    "Wadern": {"latitude": 49.5375, "longitude": 6.8786},
    "Wadgassen": {"latitude": 49.2842, "longitude": 6.8058},
    "Bous": {"latitude": 49.2828, "longitude": 6.8219},
    "Brebach-Fechingen": {"latitude": 49.2062, "longitude": 7.0169},
    "Büschfeld": {"latitude": 49.4706, "longitude": 6.8383},
    "Dirmingen": {"latitude": 49.4436, "longitude": 7.0089},
    "Dudweiler": {"latitude": 49.2742, "longitude": 7.0275},
    "Eiweiler": {"latitude": 49.4278, "longitude": 6.9064},
    "Ensheim": {"latitude": 49.1989, "longitude": 7.0667},
    "Erbach": {"latitude": 49.3219, "longitude": 7.3106},
    "Eschringen": {"latitude": 49.1986, "longitude": 7.0822},
    "Fischbach-Camphausen": {"latitude": 49.3139, "longitude": 6.9689},
    "Gersweiler": {"latitude": 49.2675, "longitude": 6.8939},
    "Heusweiler": {"latitude": 49.3586, "longitude": 6.9492},
    "Hirzweiler": {"latitude": 49.3917, "longitude": 7.0792},
    "Höchen": {"latitude": 49.3700, "longitude": 7.2736},
    "Kirkel": {"latitude": 49.2928, "longitude": 7.2672},
    "Kleinblittersdorf": {"latitude": 49.1778, "longitude": 7.0458},
    "Köllerbach": {"latitude": 49.2881, "longitude": 6.9228},
    "Landsweiler-Reden": {"latitude": 49.3622, "longitude": 7.1164},
    "Lautzkirchen": {"latitude": 49.2378, "longitude": 7.2528},
    "Ludweiler-Warndt": {"latitude": 49.2300, "longitude": 6.8447},
    "Malstatt": {"latitude": 49.2519, "longitude": 6.9708},
    "Nauweiler": {"latitude": 49.2967, "longitude": 7.1503},
    "Nennig": {"latitude": 49.5289, "longitude": 6.3769},
    "Oberbexbach": {"latitude": 49.3647, "longitude": 7.2636},
    "Ommersheim": {"latitude": 49.2308, "longitude": 7.1342},
    "Reiskirchen": {"latitude": 49.2656, "longitude": 7.0767},
    "Riegelsberg": {"latitude": 49.3147, "longitude": 6.9394},
    "Schafbrücke": {"latitude": 49.2500, "longitude": 7.0450},
    "Scheidt": {"latitude": 49.2300, "longitude": 7.0600},
    "Schwalbach": {"latitude": 49.3139, "longitude": 6.8144},
    "Sulzbach/Saar": {"latitude": 49.3061, "longitude": 7.0567},
    "Tholey": {"latitude": 49.4931, "longitude": 7.0294},
    "Wellesweiler": {"latitude": 49.3528, "longitude": 7.1997}
}

GOOGLE_MAPS_API_KEY = "AIzaSyCDKwj1fOxCW6VAQOc8djbb0mclhywXUcI"
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

# Filter data based on date and location
for i in range(len(data)-1):
    entry = data[i+1]
    city = entry["city_name"].encode('utf-8').decode('utf-8')
    parsed_date = parse_date(entry["dt_iso"])
    geocode_result = gmaps.geocode(city)
    try: 
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lon = geocode_result[0]["geometry"]["location"]["lng"]
    except IndexError:
        continue
    lat2, lon2 = float(entry["lat"]), float(entry["lon"])
    if city not in cities_in_saarland_coords: 
        continue
    if entry["weather_main"] == "Rain":
        if start_date <= parsed_date <= end_date and round(lat,2) == round(lat2,2) and round(lon,2) == round(lon2,2):
            json.dump(entry, filtered_json)
            filtered_json.write('\n')

    # Calculate percentage completed
    progress = i / (len(data) - 1) * 100

    # Calculate number of dashes to display based on progress
    num_dashes = int(progress // (100 / 30))  # Adjust 30 based on console width

    # Display progress in the console
    bar = '-' * num_dashes + ' ' * (30 - num_dashes)
    print(f'\r[{bar}] {progress:.2f}%', end='', flush=True)

print()
print("Processing completed.")