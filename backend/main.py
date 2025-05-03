

from config import INPUT_DIR, OUTPUT_DIR, ERROR_DIR, FOLIO_START, FOLIO_END, TESSERACT_CONFIG, TESSERACT_LANG
import os
from utils.init_folder import ensure_directories_exist
from services.pdf_converter import convertir_lote_pdfs
from services.preprocessing import preprocess_image
from services.ocr_reader import extract_text_from_image
from services.folio_extractor import extract_folio_from_text
from utils.logger import log_event
from utils.setup_logger import setup_logger
from utils.log_writer import write_json_log
from services.supabase_utils.supabase_logger import log_to_supabase

logger = setup_logger()


CROP_BOX= (2000, 50, 2500, 250) #ajustar despues papu

def main():
    print("Iniciado procesamiendo de documentos PDF")
    
    ensure_directories_exist()
    
    print(f"Directorio de entrada: {INPUT_DIR}")
    print(f"Rango de folios: {FOLIO_START} - {FOLIO_END}")
    
    resultados = convertir_lote_pdfs()
    
    for filename, image in resultados:
        print(f"Procesando archivo: {filename}")
        
        preprocessed = preprocess_image(image)
        pre_folio = extract_text_from_image(preprocessed)
        folio = extract_folio_from_text(pre_folio)
        
        
        if folio is not None:
            folio_num = int(folio)
            if FOLIO_START <= folio_num <= FOLIO_END:
                new_filename = f"{folio}.pdf"
                os.rename(os.path.join(INPUT_DIR, filename), os.path.join(OUTPUT_DIR, new_filename))
                log_event(new_filename, folio, "success")
                write_json_log("renames", filename, folio, "Sucess")
                log_to_supabase(new_filename, folio, "success")
                print(f"Archivo renombrado a: {new_filename}")
            else:
                print(f"Folio fuera de rango: {folio_num}")
                os.rename(os.path.join(INPUT_DIR, filename), os.path.join(ERROR_DIR, filename))
                log_event(filename, folio, "error", "Folio fuera de rango")
                write_json_log("fuera_rango", filename, folio, "Folio fuera de rango")

        else:
            print(f"Folio no válido o no detectado: {folio}")
            os.rename(os.path.join(INPUT_DIR, filename), os.path.join(ERROR_DIR, filename))
            log_event(filename, folio, "error", "No se detectó folio")
            write_json_log("no_detectado", filename, folio, "No se detectó folio")
if __name__ == "__main__":
    main()