#!/bin/bash

# Define variables
MODEL_PATH="/home/avnish/LLaVA/llava-v1.5-7b"
QUESTION_FILE="/home/avnish/LLaVA/dataset/test/questions_only.jsonl"
IMAGE_FOLDER="/home/avnish/Downloads/10499039/VQAMed2019Test/Test_Images/"
ANSWERS_FILE="/home/avnish/LLaVA/predicted_answers.jsonl"

# Run the Python script with the provided arguments
python /home/avnish/LLaVA/llava/eval/model_vqa.py \
    --model-path "$MODEL_PATH" \
    --question-file "$QUESTION_FILE" \
    --image-folder "$IMAGE_FOLDER" \
    --answers-file "$ANSWERS_FILE"
