import os
from config import INPUT_DIR, OUTPUT_DIR, ERROR_DIR, LOG_DIR

def ensure_directories_exist():
    
    for folder in [INPUT_DIR, OUTPUT_DIR, ERROR_DIR, LOG_DIR]:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Directorio creado: {folder}")
        else:
            print(f"Directorio ya existe: {folder}")