# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?

print(f"Total quakes: {data['metadata']['count']}")

# 2: How many quakes were felt by at least 100 people?


# METHOD 1
def felt_report(q):
    f = q["properties"]["felt"]
    return f is not None and f >= 100


feltreports = list(filter(felt_report, data["features"]))
print(f"Total quakes felt by at least 100 people: {len(feltreports)}")

# METHOD 2
print(
    f"Total quakes felt by at least 100 people: {sum(quake['properties']['felt'] is not None and quake['properties']['felt'] >= 100 for quake in data['features'])}"
)

# 3: Print the name of the place whose quake was felt by the most people, with the # of reports


def get_quake_felt(dataitem):
    felt = dataitem["properties"]["felt"]
    if felt is None:
        felt = 0
    return felt


mostfeltquake = max(data["features"], key=get_quake_felt)

print(
    f"The most felt quake: {mostfeltquake['properties']['title']}, reports: {mostfeltquake['properties']['felt']}"
)

# 4: Print the top 10 most significant events, with the significance value of each


def get_sig(dataitem):
    signficance = dataitem["properties"]["sig"]
    if signficance is None:
        signficance = 0
    return float(signficance)


sigevents = sorted(data["features"], key=get_sig, reverse=True)
print("The top 10 most significant events were: ")
for i in range(0, 10):
    print(
        f"Event: {sigevents[i]['properties']['title']}, Significance: {sigevents[i]['properties']['sig']}"
    )
