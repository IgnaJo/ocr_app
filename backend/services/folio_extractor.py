import re
from config import FOLIO_START, FOLIO_END

def extract_folio_from_text(text: str) -> str | None:
    # Búsqueda de patrón tipo N° 1234567 o similar
    match = re.search(r"[N№]\s*[°º]?\s*(\d{5,})", text, re.IGNORECASE)
    if match:
        return match.group(1)
    return None