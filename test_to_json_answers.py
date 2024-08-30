import os
import json
import uuid

def load_qa_pairs_with_answers(qa_file):
    qa_pairs = []
    with open(qa_file, 'r') as f:
        for line in f:
            parts = line.strip().split('|')
            if len(parts) == 4:  # Expecting image_name, some_field, question, and answer
                image_name, _, _, answer = parts
                qa_pairs.append((image_name, answer))
            else:
                print(f"Skipping invalid line in QA file: {line.strip()}")
    # Debug: Check if any QA pairs were loaded
    if not qa_pairs:
        print(f"No QA pairs with answers were loaded from {qa_file}. Please check the file format.")
    return qa_pairs

def process_and_save_answers_only(qa_pairs, output_folder, subset_name):
    # Define subset folder within output folder
    subset_folder = os.path.join(output_folder, subset_name)
    
    if not os.path.exists(subset_folder):
        os.makedirs(subset_folder)

    # Initialize list to hold all JSON data
    json_data_list = []

    # Process and save answers only
    for image_name, answer in qa_pairs:
        print(f"Processing image: {image_name}")

        # Create a unique ID for each entry
        unique_id = str(uuid.uuid4())

        # Structure for the new JSON with only id and answer
        json_data = {
            "id": unique_id,
            "answer": answer.strip()
        }

        # Append to the JSON data list
        json_data_list.append(json_data)
        print(f"Added entry with id: {unique_id} and answer: {answer}")

    # Save the JSON data list to a file
    json_output_path = os.path.join(subset_folder, 'answers_only.json')
    with open(json_output_path, 'w') as json_file:
        json.dump(json_data_list, json_file, indent=4)

    # Debug: Check if the JSON data list is empty
    if not json_data_list:
        print(f"No data was added to the JSON for {subset_name}. Please check the input files and folders.")

def save_answers_only_dataset(qa_file, output_folder, subset_name):
    # Load question-answer pairs from the text file
    qa_pairs = load_qa_pairs_with_answers(qa_file)

    # Debug: Check the number of loaded QA pairs
    print(f"Loaded {len(qa_pairs)} QA pairs with answers from {qa_file}")

    # Process and save the dataset with only answers and IDs
    process_and_save_answers_only(qa_pairs, output_folder, subset_name)

# Usage example
output_folder = 'dataset'
# train_qa_file = '/home/avnish/Downloads/10499039/ImageClef-2019-VQA-Med-Training/All_QA_Pairs_train.txt'
test_qa_file = '/home/avnish/Downloads/10499039/VQAMed2019Test/VQAMed2019_Test_Questions_w_Ref_Answers.txt'

# Save answers-only JSON
save_answers_only_dataset(test_qa_file, output_folder, 'test_answers_only')
