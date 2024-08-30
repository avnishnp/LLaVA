import json

def convert_json_to_jsonl(json_file, jsonl_file):
    # Load the JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Write the JSONL file
    with open(jsonl_file, 'w') as f:
        for entry in data:
            json_line = json.dumps(entry)
            f.write(json_line + '\n')
    
    print(f"Conversion complete. JSONL file saved as {jsonl_file}")

# Usage example
json_file = '/home/avnish/LLaVA/dataset/test_answers_only/answers_only.json'  # Path to your input JSON file
jsonl_file = '/home/avnish/LLaVA/dataset/test_answers_only/answer_only.jsonl'  # Path to your output JSONL file

convert_json_to_jsonl(json_file, jsonl_file)
