from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.requests import Request as FastAPIRequest
from app.schema.Favorite import FavoriteBuildingRequest
from app.database import get_db
from app.model.FavoriteBuilding import FavoriteBuilding


app = APIRouter()


    
@app.post("/api/favorite/buildings/{building_id}")
async def add_favorite_building(
    building_id: str,
    request: FavoriteBuildingRequest,
    db: Session = Depends(get_db)
):
    
    favorite = FavoriteBuilding(
        student_id=request.student_id,
        building_id=request.building_id,
    )
    
    db.add(favorite)
    db.commit()
    
    return {"message" : "Building added to favorites"}
    
    