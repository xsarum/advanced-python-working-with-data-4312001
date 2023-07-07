# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

import csv
import pprint


# read the contents of a CSV file into an object structure
result = []

# TODO: open the CSV file for reading
with open("Start/Ch_3/largequakes.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    sniffer = csv.Sniffer()
    sample = csvfile.read(1024) # creates a sample for the Sniffer object to work with
    csvfile.seek(0)
    if (sniffer.has_header(sample)):
        next(reader) # skips over the first row
    for row in reader:
        # print(row)
        result.append(
            {"place": row[0], "magnitude": row[1], "date": row[2], "link": row[3]}
        )


pprint.pp(result)
