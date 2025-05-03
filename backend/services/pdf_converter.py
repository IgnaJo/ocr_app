import os
from pdf2image import convert_from_path
from config import INPUT_DIR

def pdf_to_image(pdf_path: str, dpi: int = 300):
    try:
        images = convert_from_path(pdf_path, dpi=dpi, first_page=1, last_page=1)
        return images[0]
    except Exception as e:
        print(f'Error converting PDF to image: {e}')
        return None
    
def convertir_lote_pdfs():
    # Convertir todos los PDFs en la carpeta y devolver una lista de tuplas
    resultados = []
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(INPUT_DIR, filename)
            image = pdf_to_image(pdf_path)
            if image:
                resultados.append((filename, image))
    
    return resultados  
