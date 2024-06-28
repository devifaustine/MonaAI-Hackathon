import csv 
import json

csvfile = open("C:/Users/devif/PycharmProjects/MonaAI-Hackathon/data/502acf0c3bfbe29dd8496a42634e85c7.csv", "r")
jsonfile = open('data.json', 'w')


fieldnames = ("dt",	"dt_iso",	"timezone",	"city_name",	"lat",	"lon",	"temp",	"visibility",	"dew_point",
              "feels_like",	"temp_min",	"temp_max",	"pressure",	"sea_level",	"grnd_level",	"humidity",
              "wind_speed",	"wind_deg",	"wind_gust",	"rain_1h",	"rain_3h",	"snow_1h",	"snow_3h",	"clouds_all",
              "weather_id",	"weather_main", "weather_description", "weather_icon")

# convert csv to JSON
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

