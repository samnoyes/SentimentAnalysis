import json
import csv
import sys

# Function to convert CSV dataset to textcat annotation JSONL format
def convert_csv_to_json(csv_file, jsonl_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        data = csv.reader(file)
        next(data)  # Skip the header row
        
        with open(jsonl_file, "w") as output_file:
            for row in data:
                sentence = row[0]
                sentiment = float(row[1])

                # Create the example object with text and label
                example = {
                    "text": sentence,
                    "cats": {
                        "positive": sentiment,
                        "negative": 1.0 - sentiment
                    }
                }

                # Write each example as a separate line in the JSONL file
                output_file.write(json.dumps(example) + "\n")

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py <input_csv_file> <output_jsonl_file>")
else:
    # Get the input and output file paths from command-line arguments
    input_csv_file = sys.argv[1]
    output_jsonl_file = sys.argv[2]

    # Convert the CSV dataset to textcat annotation JSONL format
    convert_csv_to_json(input_csv_file, output_jsonl_file)
