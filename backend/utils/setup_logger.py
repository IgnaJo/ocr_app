import logging  
from logging.handlers import TimedRotatingFileHandler    
from config import LOG_DIR
import os

def setup_logger(name="folio_logger" ):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    
    if logger.hasHandlers():
        return logger
    
    log_path = os.path.join(LOG_DIR, "process_log.txt")
    
    handler = TimedRotatingFileHandler(
        log_path,
        when="midnight", 
        interval=1, 
        backupCount=30,
        encoding="utf-8"
    )
    
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger