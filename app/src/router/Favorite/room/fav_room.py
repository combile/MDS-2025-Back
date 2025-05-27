from fastapi import APIRouter, Depends, HTTPException
from app.schema.Favorite import FavoriteRoomRequest
from app.model.FavoriteRoom import FavoriteRoom as FavoriteRoomModel #SQLAlchemy 모델
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.requests import Request as FastAPIRequest

app = APIRouter()


#즐겨찾기 추가
@app.post("/api/favorite/rooms")
async def add_favorite_room(
    request: FavoriteRoomRequest,
    db: Session = Depends(get_db)
):
    
    #SQLAlchemy 모델 인스턴스 생성
    favorite_room = FavoriteRoomModel(
        student_id = request.student_id,
        room_id = request.room_id,
        building_id = request.building_id
    )
    
    #DB 추가
    db.add(favorite_room)
    db.commit()
    
    return {"message": "Room added to favorites"}