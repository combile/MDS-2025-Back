from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base



class FavoriteBuilding(Base):
    __tablename__ = "FavoriteBuilding"
    
    student_id = Column(String, ForeignKey("User.student_id"), nullable=False, primary_key=True)
    building_id = Column(String, ForeignKey("Building.building_id"), nullable=False)
    
    #Relationship - total 2
    favoritebuilding_with_user = relationship("User",back_populates="user_with_favoritebuilding")
    favoritebuilding_with_building = relationship("Building", back_populates="building_with_favoritebuilding")