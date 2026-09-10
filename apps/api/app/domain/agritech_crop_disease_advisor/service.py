from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.agritech_crop_disease_advisor.models import AgenticAgritechCropDiseaseAdvisorSession, AgenticAgritechCropDiseaseAdvisorItem
from app.domain.agritech_crop_disease_advisor.schemas import AgenticAgritechCropDiseaseAdvisorSessionCreate, AgenticAgritechCropDiseaseAdvisorItemCreate

class AgenticAgritechCropDiseaseAdvisorService:
    @staticmethod
    def create_session(db: Session, data: AgenticAgritechCropDiseaseAdvisorSessionCreate) -> AgenticAgritechCropDiseaseAdvisorSession:
        db_obj = AgenticAgritechCropDiseaseAdvisorSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticAgritechCropDiseaseAdvisorSession:
        return db.query(AgenticAgritechCropDiseaseAdvisorSession).filter(AgenticAgritechCropDiseaseAdvisorSession.id == session_id).first()
