from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.requests import Request as FastAPIRequest
from app.schema.Favorite import FavoriteBuildingRequest
from app.database import get_db
from app.model.FavoriteBuilding import FavoriteBuilding

app = APIRouter()

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: FastAPIRequest, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error":exc.detail}
    )
    
    
@app.delete("/api/favorite/buildings/{building_id}")
async def remove_favorite_building(
    request: FavoriteBuildingRequest,
    db: Session = Depends(get_db)
):
    favorite = db.query(FavoriteBuilding).filter_by(
        student_id=request.student_id,
        building_id=request.building_id
    ).first()
    
    if not favorite:
        raise HTTPException(
            status_code=404,
            detail="Favorite building not found"
        )
        
    db.delete(favorite)
    db.commit()
    
    return {"message":"Building removed from favorites"}