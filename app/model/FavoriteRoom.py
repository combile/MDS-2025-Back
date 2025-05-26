from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class FavoriteRoom(Base):
    __tablename__ = "FavoriteRoom"
    
    student_id = Column(String, ForeignKey("User.student_id"),primary_key=True)
    room_id = Column(String,ForeignKey("Room.room_id"), primary_key=True)
    
    #Relationship: -total 2
    favoriteroom_with_user = relationship("User", back_populates="user_with_favoriteroom")
    favoriteroom_with_room = relationship("Room", back_populates="room_with_favoriteroom")