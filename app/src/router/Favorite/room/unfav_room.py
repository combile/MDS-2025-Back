from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.model.FavoriteRoom import FavoriteRoom as FavoriteRoomModel #SQLAlchemy 모델
from fastapi.responses import JSONResponse
from fastapi.requests import Request as FastAPIRequest
from app.database import get_db
from app.schema.Favorite import FavoriteRoomRequest

app = APIRouter()


    
@app.delete("/api/favorite/rooms/{room_id}")
async def remove_favorite_room(
    request: FavoriteRoomRequest,
    db: Session = Depends(get_db)
):
    
    favorite = db.query(FavoriteRoomModel).filter_by(
        student_id = request.student_id,
        room_id = request.room_id
    ).first()
    
    if not favorite:
        raise HTTPException(
            status_code=404,
            detail="Favorite room not found"
        )
    
    db.delete(favorite)
    db.commit()
    
    return {"message":"Room removed from favorites"}