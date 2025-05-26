from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request as FastAPIRequest
from sqlalchemy.orm import Session
from app.schema.Room import Room as RoomSchema #pydnantic 모델
from app.model.Room import Room #SQlAlchemy 모델 임포트
from app.database import get_db

app = APIRouter()

#MARK: - 커스텀 예외 핸들러
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: FastAPIRequest, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error":exc.detail}
    )
    
    
@app.get("/api/rooms")
async def get_all_room(building_id: str, db: Session = Depends(get_db)):
    
    rooms = db.query(Room).filter(Room.building_id==building_id).all()
        
    if not rooms:
        raise HTTPException(
            status_code=404,
            detail="No rooms found in this building"
        )
        
    result = [RoomSchema.from_orm(room) for room in rooms]
    return result