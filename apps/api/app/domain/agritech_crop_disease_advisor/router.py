from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.agritech_crop_disease_advisor.schemas import AgenticAgritechCropDiseaseAdvisorSessionCreate, AgenticAgritechCropDiseaseAdvisorSessionResponse
from app.domain.agritech_crop_disease_advisor.service import AgenticAgritechCropDiseaseAdvisorService

router = APIRouter(prefix="/api/v1/agritech_crop_disease_advisor", tags=["Agentic Agritech Crop Disease Advisor Domain"])

@router.post("/sessions", response_model=AgenticAgritechCropDiseaseAdvisorSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticAgritechCropDiseaseAdvisorSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Agritech Crop Disease Advisor.
    """
    return AgenticAgritechCropDiseaseAdvisorService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticAgritechCropDiseaseAdvisorSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticAgritechCropDiseaseAdvisorService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
