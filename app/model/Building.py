from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class Building(Base):
    __tablename__ = "Building"
    
    building_id = Column(String,primary_key=True,nullable=False)
    name = Column(String, nullable=False, unique=True)
    location = Column(String, nullable=False, unique=True)
    is_available = Column(Boolean, server_default=False)
    
    #Relation
    building_with_Room = relationship("Room", back_populates="room_with_building")