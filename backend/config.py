import os


# Directorios de archivos pdf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_DIR = os.path.join(BASE_DIR, 'input')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
ERROR_DIR = os.path.join(BASE_DIR, 'error')
LOG_DIR = os.path.join(BASE_DIR, 'logs')



# Rangos de folios esperados

FOLIO_START = 3869525
FOLIO_END = 3879525

# OCR - Tesseract
TESSERACT_CONFIG = '--oem 3 --psm 6'
TESSERACT_LANG = 'spa+eng'

# SUPABASE CONFIG
SUPABASE_URL = os.getenv('SUPABASE_URL', ' ')
SUPABASE_KEY = os.getenv('SUPABASE_KEY', ' ')
SUPABASE_LOG_TABLE = 'logs'

