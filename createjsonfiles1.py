#create file2
import json

# Sample JSON data for file2
data = [
   {
       "Student Adm No.": 192099,
       "Student Name": "Clara Ravis",
       "Date of Birth": 2007
   },
   {
       "Student Adm No.": 156745,
       "Student Name": "Tom Denton James",
       "Date of Birth": 2006
   }
]

# Specify the output file name
output_file = "file2.json"

# Save the data to a JSON file
with open(output_file, "w") as json_file:
   json.dump(data, json_file, indent=4)
