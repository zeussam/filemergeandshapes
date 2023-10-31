#create file1

import json

# Sample JSON data
data = [
    {
        "Student Adm No.": 192098,
        "Student Name": "John Doe Hurt",
        "Date of Birth": 2003
    },
    {
        "Student Adm No.": 156789,
        "Student Name": "Susan Muhia Wanja",
        "Date of Birth": 2004
    }
]

# Specify the output file name
output_file = "file1.json"

# Save the data to a JSON file
with open(output_file, "w") as json_file:
    json.dump(data, json_file, indent=4)


