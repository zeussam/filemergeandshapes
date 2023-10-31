import pandas as pd

def merge_json_files(file1, file2):
    data1 = pd.read_json(file1)
    data2 = pd.read_json(file2)
    merged_data = pd.concat([data1, data2], ignore_index=True)
    return merged_data

if __name__ == "__main__":
    file1 = "file1.json"
    file2 = "file2.json"
    merged_data = merge_json_files(file1, file2)
    merged_data.to_json("output/merged_data.json", orient="records")
