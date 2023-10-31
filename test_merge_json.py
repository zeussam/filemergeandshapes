import unittest
from merge_json import merge_json_files

class TestMergeJSON(unittest.TestCase):
    def test_merge_json(self):
        file1 = "file1.json"
        file2 = "file2.json"
        merged_data = merge_json_files(file1, file2)
        self.assertEqual(len(merged_data), 4)  # Adjust as needed

if __name__ == "__main__":
    unittest.main()

