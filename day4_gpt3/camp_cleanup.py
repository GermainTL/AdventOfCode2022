# Code généré avec GPT3

import csv

counter = 0

# Parse the input file to extract the section assignment pairs
with open("day4_gtp3/input/input.txt", "r") as input_file:
    reader = csv.reader(input_file, delimiter=",")
    for ranges in reader:
        # Parse the start and end values for each range
        start1 = int(ranges[0].split("-")[0])
        end1 = int(ranges[0].split("-")[1])
        start2 = int(ranges[1].split("-")[0])
        end2 = int(ranges[1].split("-")[1])

        # Check if one range fully contains the other
        if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
            counter += 1

# Print the final value of the counter
print(counter)
