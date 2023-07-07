# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import defaultdict


# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# write a program that produces the type of event along with number of times occurred in data file. 


event_counter = defaultdict(int)

for event in data['features']:
    event_counter[event['properties']['type']] += 1

for k,v in event_counter.items():
    print(f"{k:15}: {v}")
