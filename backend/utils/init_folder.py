import os
from config import INPUT_DIR, OUTPUT_DIR, ERROR_DIR, LOG_DIR

def ensure_directories_exist(input_dir: str, output_dir: str):
    
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)