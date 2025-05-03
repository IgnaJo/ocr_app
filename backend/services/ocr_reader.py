import pytesseract
from config import TESSERACT_CONFIG, TESSERACT_LANG

def extract_text_from_image(image) -> str:
    #estrar texto de la imagen preprocesada
    
    try:
        text = pytesseract.image_to_string(image, config=TESSERACT_CONFIG, lang=TESSERACT_LANG)
        cleaned_text = text.strip().replace(" ", "").replace("\n", "")
        if cleaned_text.startswith("N"):
            cleaned_text = cleaned_text[1:] #quitar prefijo N de la cadena de folio
        return cleaned_text
    except Exception as e:
        print(f'Error extracting text from image: {e}')
        return ""