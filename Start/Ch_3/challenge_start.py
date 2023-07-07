# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD


def get_sig(dataitem):
    sig = dataitem["properties"]["sig"]
    return 0 if sig is None else sig


sig_events = sorted(
    data["features"], key=get_sig, reverse=True
)  # this sorts the data coming from the get_sig function
sig_events = sig_events[:40]  # this gets the top 40
sig_events.sort(
    key=lambda e: e["properties"]["time"], reverse=True
)  # this sorts the top 40 by time


header = ["Magnitude", "Place", "Felt Reports", "Date", "Google Map Link"]
rows = []


for event in sig_events:
    thedate = datetime.date.fromtimestamp(int(event["properties"]["time"] / 1000))
    latitude = event["geometry"]["coordinates"][1]
    longitude = event["geometry"]["coordinates"][0]
    gmap_link = (
        f"https://www.google.com/maps/search/?api=1&query={latitude}%2C{longitude}"
    )
    rows.append(
        [
            event["properties"]["mag"],
            event["properties"]["place"],
            0 if event["properties"]["felt"] is None else event["properties"]["felt"],
            thedate,
            gmap_link,
        ]
    )


with open("Start/Ch_3/Top_40_Seismic_Events.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)
