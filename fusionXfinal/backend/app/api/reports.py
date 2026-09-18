from fastapi import APIRouter, Depends

from app.api.auth import get_current_user

router = APIRouter()


@router.post("/reports")
def create_report(payload: dict, user=Depends(get_current_user)):
    return {"id": "report-001", "status": "generated", "report": payload}


@router.get("/reports/{report_id}")
def get_report(report_id: str, user=Depends(get_current_user)):
    return {"id": report_id, "summary": "Energy report generated successfully", "download_url": f"/reports/{report_id}.pdf"}
