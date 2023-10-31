import json
from typing import List, Dict, Any

# question 1
def read_jsonline(FILEPATH: str) -> List[Dict[str, Any]]:
    with open(FILEPATH, "r") as f:
        first_json_line = f.readline()
        shape_coordinates = json.loads(first_json_line)
        return shape_coordinates

    #answers:file imports used: json,typing,