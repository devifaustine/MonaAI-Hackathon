import csv
import json 

# converts csv file for firestations.csv to JSON -> firestations JSON
# Initialize an empty list to store weather data
firestation = []

csvfile = "C:/Users/devif/PycharmProjects/MonaAI-Hackathon/data/fire_stations_locations/fire_stations/csv of fire stations.csv"
fireworkers_json = open('fireworkers.json', 'w')

# Define field names
fieldnames = ['business_status', 'geometry/location/lat', 'geometry/location/lng', 'geometry/viewport/south',
              'geometry/viewport/west', 'geometry/viewport/north', 'geometry/viewport/east', 'icon',
              'icon_background_color', 'icon_mask_base_uri', 'name', 'place_id', 'plus_code/compound_code',
              'plus_code/global_code', 'rating', 'reference', 'scope', 'types/0', 'types/1', 'types/2',
              'user_ratings_total', 'vicinity', 'photos/0/height', 'photos/0/html_attributions/0', 'photos/0/width',
              'opening_hours/open_now', 'permanently_closed', 'types/3', 'types/4']

# List to store JSON objects
json_objects = []

# Read CSV file and convert to JSON objects
# List of encodings to try
encodings = ['utf-8', 'latin1', 'ISO-8859-1']

# Try reading the file with different encodings
for encoding in encodings:
    try:
        with open(csvfile, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=',')
            # Skip header row
            next(csv_reader)  # skip the header row
            for line in csv_reader:
                # Create a dictionary from the row data using fieldnames
                data_dict = {fieldnames[i]: line[i] if i < len(line) else '' for i in range(len(fieldnames))}
                
                # Append the dictionary to the list
                json_objects.append(data_dict)
        break  # If reading is successful, break out of the loop
    except UnicodeDecodeError as e:
        print(f"Encoding {encoding} failed: {e}")
        continue

# Write JSON objects to a JSON file
for i in json_objects:
    json.dump(i, fireworkers_json)
    fireworkers_json.write('\n')

print(f"Successfully wrote JSON objects to {fireworkers_json}")

