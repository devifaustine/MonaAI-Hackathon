import csv
import json

# converts csv file for rainToSkillTabel.csv to JSON -> rainToSkill JSON
# Initialize an empty list to store weather data
weather_data = []

csvfile = open("C:/Users/devif/PycharmProjects/MonaAI-Hackathon/data/rainToSkillTabel.csv", "r", newline='')
jsonfile = open('rainToSkill.json', 'w')

fieldnames = ("Weather Description", "Required Skill Level", "amount of rain")

# convert csv to JSON
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

# Convert to JSON
json_data = json.dumps(weather_data, indent=2)
