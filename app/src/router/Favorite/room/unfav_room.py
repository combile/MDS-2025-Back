from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.model.FavoriteRoom import FavoriteRoom as FavoriteRoomModel #SQLAlchemy 모델
from fastapi.responses import JSONResponse
from fastapi.requests import Request as FastAPIRequest
from app.database import get_db
from app.schema.Favorite import FavoriteRoomRequest

app = APIRouter()

#MARK: - 커스텀 예외 핸들러
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: FastAPIRequest, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error":exc.detail}
    )
    
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