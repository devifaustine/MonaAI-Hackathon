import csv
import json

# converts csv file for rainToSkillTabel.csv to JSON -> rainToSkill JSON
# Initialize an empty list to store weather data
weather_data = []

csvfile = "C:/Users/devif/PycharmProjects/MonaAI-Hackathon/data/rainToSkillTabel.csv"
rainToSkill_json = open('rainToSkill.json', 'w')

# Define field names
fieldnames = ["Weather Description", "Required Skill Level", "amount of rain"]

# List to store JSON objects
json_objects = []

# Read CSV file and convert to JSON objects
with open(csvfile, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=';')
    # Skip header row
    next(csv_reader)  # skip the header row
    for row in csv_reader:
        # Extract components
        weather_description = row[0]
        required_skill_level = row[1]
        amount_of_rain = row[2]
        
        # Handle '-' as None for amount of rain
        if amount_of_rain == '-':
            amount_of_rain = None
        
        # Create dictionary for JSON object
        json_obj = {
            fieldnames[0]: weather_description,
            fieldnames[1]: required_skill_level,
            fieldnames[2]: amount_of_rain
        }
        
        # Append JSON object to list
        json_objects.append(json_obj)

# Write JSON objects to a JSON file
for i in json_objects:
    json.dump(i, rainToSkill_json)
    rainToSkill_json.write('\n')

print(f"Successfully wrote JSON objects to {rainToSkill_json}")
