from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.requests import Request as FastAPIRequest
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.Building import Building as BuildingSchema
from app.model.Building import Building as BuildingModel #SQLAlchemy 모델 임포트


app = APIRouter()


    
@app.get("/api/buildings")
async def get_building(db: Session = Depends(get_db)):
    try:
        #SQLAlchemy 모델 임포트
        buildings = db.query(BuildingModel).all()
        
        #pydantic 모델 변환
        result = [BuildingSchema.from_orm(b) for b in buildings]
        return result
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Invaglid credentials"
        )