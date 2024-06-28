import json 
import math

"""
Task 4: Team Matching

1. Match the best teams to the emergencies based on required skills, team size, and availability 
considering the time of the day, travel time, and distance.

2. Ensure that the teams assigned to each emergency have the necessary skills and are the closest in proximity 
to the emergency location to optimize response time.

"""

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

def near(loc1, loc2): 
    return point_within_distance_of_river(loc1[0], loc1[1], loc2, max_distance_km=10)

def find_available(arr, location):
    for f in arr: 
        available = f["opening_hours/open_now"]
        f_loc = [(float(f["geometry/viewport/south"]), float(f["geometry/viewport/west"])), 
                 (float(f["geometry/viewport/north"]), float(f["geometry/viewport/east"]))]
        if available == "true" and near(location, f_loc): 
            f["opening_hours/open_now"] = "false"
            return f

def find_firefighter(skill, flood):
    """
    Finding a firefighter with skill accordingly 
    """
    location = (float(flood["lat"]), float(flood["lon"]))
    if skill == "Advanced":
        ff = find_available(working, location)
        if ff is None: 
            ff = find_available(voluntary, location)
        return ff
    elif skill == "Intermediate": 
        ff = find_available(voluntary, location)
        return ff
    else: 
        raise Exception("Skill not available.")

voluntary = []
working = []

flood_location = []
assignments = []

# digest all json objects -> flood locations and firefighters
with open('available_fireworkers.json', 'r') as f: 
    for line in f: 
        try: 
            fireman = json.loads(line)
            if fireman["freiwillig_alt"]: 
                voluntary.append(fireman)
            else: 
                working.append(fireman)
        except json.JSONDecodeError as e: 
            print(f"Error decoding JSON: {e}")

with open('possible_flood.json', 'r') as locations: 
    for loc in locations: 
        try: 
            flood_location.append(json.loads(loc))
        except json.JSONDecodeError as e: 
            print(f"Error decoding JSON: {e}")

for flood in flood_location:
    if "Advanced" in flood["requried_skill"]:
        for i in range(20):
            firefighter = find_firefighter('Advanced', flood)
            assignment = {
                "place_id": firefighter["place_id"], 
                "location": flood["city_name"]
            }
    else:  # case intermediate required 
        for i in range(20):
            firefighter = find_firefighter('Intermediate', flood)
            print(firefighter)
            assignment = {
                "place_id": firefighter["place_id"], 
                "location": flood["city_name"]
            }
    assignments.append(assignment)

print(assignments)
    
