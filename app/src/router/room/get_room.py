from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.requests import Request as FastAPIRequest
from app.model.Room import Room as RoomModel #SQLAlchemy 모델
from app.schema.Room import Room as RoomSchema #Pydantic 모델
from app.database import get_db

app = APIRouter()


@app.get("/api/rooms/{room_id}")
async def get_room(room_id: str, db: Session = Depends(get_db)):
    room = db.query(RoomModel).filter(RoomModel.room_id == room_id).first()
    
    if not room:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )
        
    result = RoomSchema.from_orm(room)
    return result