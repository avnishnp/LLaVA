import os
import json
import uuid
from PIL import Image

def find_image_with_extension(images_folder, image_name_base, extension=".jpg"):
    # Construct the image path by appending the extension
    image_path = os.path.join(images_folder, image_name_base + extension)
    if os.path.exists(image_path):
        return image_path
    return None

def process_and_save_from_local(images_folder, qa_pairs, output_folder, subset_name):
    # Define image subfolder within output folder
    subset_folder = os.path.join(output_folder, subset_name)
    
    if not os.path.exists(subset_folder):
        os.makedirs(subset_folder)

    # Initialize list to hold all JSON data
    json_data_list = []

    # Process and save images and labels
    for image_name, question, answer in qa_pairs:
        print(f"Processing image: {image_name}")

        # Find the image file with the .jpg extension
        image_path = find_image_with_extension(images_folder, image_name)

        if not image_path:
            print(f"Image {image_name} not found in {images_folder}, skipping.")
            continue

        # Load image
        try:
            image = Image.open(image_path)
        except Exception as e:
            print(f"Error loading image {image_name}: {e}")
            continue

        # Create a unique ID for each image
        unique_id = str(uuid.uuid4())

        # The line below is commented out to prevent saving the image again
        # new_image_path = os.path.join(image_subfolder, f"{unique_id}.jpg")

        # Remove duplicates and format answers
        unique_answers = list(set(answer.split(',')))
        formatted_answers = ", ".join(unique_answers)

        # Structure for LLaVA JSON
        json_data = {
            "id": unique_id,
            "image": f"{image_name}.jpg",  # Use the original image name
            "conversations": [
                {
                    "from": "human",
                    "value": question
                },
                {
                    "from": "gpt",
                    "value": formatted_answers
                }
            ]
        }

        # Append to the JSON data list
        json_data_list.append(json_data)
        print(f"Added entry for image {image_name} with question: {question} and answer: {formatted_answers}")

    # Save the JSON data list to a file
    json_output_path = os.path.join(subset_folder, 'dataset.json')
    with open(json_output_path, 'w') as json_file:
        json.dump(json_data_list, json_file, indent=4)

    # Debug: Check if the JSON data list is empty
    if not json_data_list:
        print(f"No data was added to the JSON for {subset_name}. Please check the input files and folders.")

def load_qa_pairs(qa_file):
    qa_pairs = []
    with open(qa_file, 'r') as f:
        for line in f:
            parts = line.strip().split('|')
            if len(parts) == 3:
                image_name, question, answer = parts
                qa_pairs.append((image_name, question, answer))
            else:
                print(f"Skipping invalid line in QA file: {line.strip()}")
    # Debug: Check if any QA pairs were loaded
    if not qa_pairs:
        print(f"No QA pairs were loaded from {qa_file}. Please check the file format.")
    return qa_pairs

def save_dataset_from_local(images_folder, qa_file, output_folder, subset_name):
    # Load question-answer pairs from the text file
    qa_pairs = load_qa_pairs(qa_file)

    # Debug: Check the number of loaded QA pairs
    print(f"Loaded {len(qa_pairs)} QA pairs from {qa_file}")

    # Process and save the dataset using the local images and QA pairs
    process_and_save_from_local(images_folder, qa_pairs, output_folder, subset_name)

# Usage example
output_folder = 'dataset'
train_images_folder = '/home/avnish/Downloads/10499039/ImageClef-2019-VQA-Med-Training/Train_images'
test_images_folder = '/home/avnish/Downloads/10499039/VQAMed2019Test/Test_Images'
train_qa_file = '/home/avnish/Downloads/10499039/ImageClef-2019-VQA-Med-Training/All_QA_Pairs_train.txt'
test_qa_file = '/home/avnish/Downloads/10499039/VQAMed2019Test/VQAMed2019_Test_Questions.txt'

save_dataset_from_local(train_images_folder, train_qa_file, output_folder, 'train')
# save_dataset_from_local(test_images_folder, test_qa_file, output_folder, 'test')
