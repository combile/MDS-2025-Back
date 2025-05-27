from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
# from app.model.User import User
# from app.model.FavoriteBuilding import FavoriteBuilding 
# from app.model.Room import Room 


class Building(Base):
    __tablename__ = "Building"
    
    building_id = Column(String,primary_key=True,nullable=False)
    name = Column(String, nullable=False, unique=True)
    location = Column(String, nullable=False, unique=True)
    is_available = Column(Boolean, server_default="false")#NOTE: - SQL에서 "false"로 표기
    
    #Relationship - total 2
    building_favoritebuilding_user = relationship("User", secondary="FavoriteBuilding", back_populates="user_favoritebuilding_building")
    building_with_favoritebuilding = relationship("FavoriteBuilding", back_populates="favoritebuilding_with_building") #join table
    
    building_with_room = relationship("Room", back_populates="room_with_building")

    