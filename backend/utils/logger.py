import os 
import json
from datetime import datetime
from config import LOG_DIR

TEXT_LOG_FILE = os.path.join(LOG_DIR, 'process_log.txt')
JSON_LOG_FILE = os.path.join(LOG_DIR, 'proscess_log.jsonl')


def log_event(filename, folio, status, message=""):
    timestamp = datetime.now().isoformat(timespec='seconds')
    
    #texto normal
    text_line = f"[{timestamp}] {filename} Archivo: {filename} -> Folio: {folio} -> status: {status.upper()} {f'->{message}' if message else ''}"
    with open(TEXT_LOG_FILE, 'a', encoding="utf-8") as text_file:
        text_file.write(text_line + '\n')
        
    #json
    json_entry = {
        "timestamp": timestamp,
        "filename":  filename,
        "folio": folio,
        "status": status,
        "message": message
    }
    
    with open(JSON_LOG_FILE, 'a', encoding="utf-8") as json_file:
        json_file.write(json.dumps(json_entry) + '\n')
