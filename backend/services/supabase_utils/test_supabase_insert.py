from datetime import datetime
from services.supabase_utils.supabase_client import supabase

def test_log_insert():
    try:
        data = {
            "filename": "test_file.pdf",
            "folio": "123456",
            "status": "test",
            "timestamp": datetime.now().isoformat()
        }
        response = supabase.table("document_logs").insert(data).execute()
        print("[TEST] Inserción exitosa:", response)
    except Exception as e:
        print("[TEST] Error al insertar:", e)

if __name__ == "__main__":
    test_log_insert()
