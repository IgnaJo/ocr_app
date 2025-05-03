import json
import os
from datetime import datetime
from config import LOG_DIR

def write_json_log(event_type, filename, folio=None, message=None):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "filename": filename,
        "folio": folio,
        "message": message
    }
    
    log_file = os.path.join(LOG_DIR, "process_log.json")
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")