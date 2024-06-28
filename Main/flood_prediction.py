import json
import math 
import re 

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the Earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of Earth in kilometers (approximately 6371 km)
    radius_of_earth = 6371.0 
    
    # Calculate the distance
    distance = radius_of_earth * c
    
    return distance

def point_within_distance_of_river(point_lat, point_lon, river_coordinates, max_distance_km):
    """
    Check if a point is within a specified distance (in kilometers) of a river.
    Returns True if the point is within the distance, False otherwise.
    """
    for river_lat, river_lon in river_coordinates:
        distance_to_river = haversine(point_lat, point_lon, river_lat, river_lon)
        if distance_to_river <= max_distance_km:
            return True
    return False
    

def isDanger(data): 
    """
    checks the fatality of the rain according to rainToSkill.json 
    """
    if data["requried_skill"] in ["Intermediate Skills", "Advanced Skills"]:
        return True
    return False

# Flood Zone Prediction
# Using the processed rainfall data, predict potential flood zones. For simplicity, 
# assume a basic threshold model where areas receiving more than a certain amount of rainfall 
# within a specific time frame are at risk of flooding.
# The threshold values can be predefined (e.g., 50mm of rainfall in 24 hours).

rainToSkill = []
data = []
possibleFlood = open('possible_flood.json', 'w')

# Saarriver + Bliesriver source and mouth coordinates  
saar_river_coordinates = [
    (48.32, 7.95), 
    (49.42, 6.34), 
]
blies_river_coordinates = [
    (49.31, 7.24), 
    (49.652, 7.40)
]

# process the JSON data from rainToSkill.json and filtered_data.json
with open('rainToSkill.json', 'r') as f:
    for line in f:
        try:
            rainToSkill.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

with open('filtered_data.json', 'r') as f: 
    for line in f: 
        try: 
            data.append(json.loads(line))
        except json.JSONDecodeError as e: 
            print(f"Error decoding JSON: {e}")

def assign_skill(rain): 
    """
    assign required level skill according to rainfall 
    """
    regex = r"(?:\d+\s*-\s*\d+)|<(?:\s*\d+)|>(?:\s*\d+)"
    pattern = re.compile(regex)
    for s in rainToSkill: 
        match = pattern.search(s[""])
        if match: 
            return s["Required Skill Level"]


def find(desc): 
    """
    find the required levels in rainToSkill
    """
    for s in rainToSkill: 
        if s['Weather Description'] == desc: 
            return s["Required Skill Level"]

for i in range(len(data)):
    # check position near both Saar and Blies river and required skill 
    lat = float(data[i]["lat"])
    lon = float(data[i]["lon"])
    desc = data[i]["weather_description"]
    data[i]["requried_skill"] = find(desc)
    print(data[i]["requried_skill"])
    is_within_5km_saar = point_within_distance_of_river(lat, lon, saar_river_coordinates, max_distance_km=5)
    is_within_5km_blies = point_within_distance_of_river(lat, lon, blies_river_coordinates, max_distance_km=5)
    if is_within_5km_blies or is_within_5km_saar or isDanger(data[i]): 
        json.dump(data[i], possibleFlood)
        possibleFlood.write('\n')

