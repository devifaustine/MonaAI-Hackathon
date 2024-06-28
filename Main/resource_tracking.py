import json

"""
3. Resource Tracking
- Maintain a list of emergency response resources (e.g., rescue boats, medical supplies, personnel) along 
with their current status (available, deployed, under maintenance) and location.
- The program should be able to update the status and location of these resources dynamically.
"""

firestations = []
working_fireworkers_json = open('available_fireworkers.json', 'w')

# process the JSON data
with open('fireworkers.json', 'r') as f:
    for line in f:
        try:
            firestations.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

fireworker = []

# sort the firestations with fulltime fireworkers and voluntary 
for f in firestations:
    name = f["name"]
    if f["permanently_closed"]:  # fireman not working anymore 
        continue
    if "Freiwillige" in name or "Alt" in name:
        f["freiwillig_alt"] = True
    else: 
        f["freiwillig_alt"] = False
    fireworker.append(f)
    
for i in fireworker:
    json.dump(i, working_fireworkers_json)
    working_fireworkers_json.write('\n')

print("Finish processing and fireworkers data.")