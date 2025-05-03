from datetime import datetime
from .supabase_client import supabase

def log_to_supabase(filename: str, folio: int, status: str):
    try:
        data = {
            "filename": filename,
            "folio": folio,
            "status": status,
            "timestamp": datetime.now().isoformat()
        }
    
        supabase.table('document_logs').insert(data).execute()
        print(f"[SUPABASE] log enviado: {data}")
    except Exception as e:
        print(f"[SUPABASE] Error al enviar log: {e}")