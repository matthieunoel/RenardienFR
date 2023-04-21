import os
import json

input_file = "./fr_FR.txt"
output_file = "./fr_FR.json"

# check if output file exists and delete it if it does
if os.path.exists(output_file):
    os.remove(output_file)

# read input file
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# create JSON array
data = {"data": []}
for line in lines:
    array = line.strip().replace("\n", "").split("	")

    if ", " in array[1]:
        res = array[1].split(", ")
        array[1] = max(res, key=len)

    array[1] = array[1].replace(",", " ").replace(" ", " ").replace("ː", " ").replace("ʼ", " ")

    if not ' ' in array[0]:
        data["data"].append(array)

# write output file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f)