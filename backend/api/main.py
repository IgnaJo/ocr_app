from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
frpm typing import List, Optional
from datetime import datetime
from services.supabase_utils.supabase_client import supabase


app = FastAPI(title="Document Processing API", description="API for processing and logging document information", version="1.0")

class LogEntry(BaseModel):
    filename: str
    folio: int
    status: str
    timestamp: datetime = datetime.now()
    
    
@app.post("/log")
def log_document(entry: LogEntry):
    try:
        data = entry.dict()
        supabase.table("document_logs").insert(data).execute()
        return {"message": "Log entry created successfully", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inserting log entry: {e}")
    
    
@app.get("/logs/", response_model=List[dict])
def get_logs(
    folio: Optional[str] = None,
    status: Optional[str] = None,
    start_date: Optional[datetime] = Query(None, description="Formato: YYYY-MM-DD"),
    end_date: Optional[datetime] = Query(None, description="Formato: YYYY-MM-DD"),
):
    try:
        query = supabase.table("document_logs").select("*")
        
        if folio:
            query = query.eq("folio", folio)
        if status:
            query = query.eq("status", status)
        if start_date:
            query = query.gte("timestamp", f"{start_date}T00:00:00")
        if end_date:
            query = query.lte("timestamp", f"{end_date}T23:59:59")
        response = query.execute()
        
        if "data" in response and isinstance(response["data"], list):
            return response["data"]
        else:
            raise HTTPException(status_code=500, detail="Error en comunicacion con Supabase")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching logs: {e}")
        