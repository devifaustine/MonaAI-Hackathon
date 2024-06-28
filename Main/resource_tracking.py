import json

"""
3. Resource Tracking
- Maintain a list of emergency response resources (e.g., rescue boats, medical supplies, personnel) along 
with their current status (available, deployed, under maintenance) and location.
- The program should be able to update the status and location of these resources dynamically.
"""

firestations = []

# process the JSON data
with open('fireworkers.json', 'r') as f:
    for line in f:
        try:
            firestations.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

real = []
freiwillig = []

# sort the firestations with fulltime fireworkers and voluntary 
for f in firestations:
    if "Freiwillige" in f["name"]:
        freiwillig.append(f)
    else: 
        real.append(f)

