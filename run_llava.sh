#!/bin/bash

# Define variables
MODEL_PATH="/home/avnish/LLaVA/checkpoints/llava-v1.5-13b-task-lora"
MODEL_BASE="/home/avnish/LLaVA/llava-v1.5-7b"
IMAGE_FILE="/home/avnish/Downloads/10499039/VQAMed2019Test/VQAMed2019Test/VQAMed2019_Test_Images/synpic24739.jpg"
QUERY="what is the mr weighting in this image?"

# Run the command
python /home/avnish/LLaVA/llava/eval/run_llava.py --model-path "$MODEL_PATH" --model-base "$MODEL_BASE" --image-file "$IMAGE_FILE" --query "$QUERY"
