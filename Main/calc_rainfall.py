import json 

"""
calculates average rainfall over different regions
"""

states = []

with open('filtered_data.json', 'r') as f: 
    for line in f: 
        try: 
            data = json.loads(line)
            if data["city_name"] not in states: 
                states.append([data["city_names"]])
        except json.JSONDecodeError as e: 
            print(f"Error decoding JSON: {e}")

