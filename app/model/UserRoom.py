from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base



class UserRoom(Base):
    __tablename__ = "UserRoom"
    
    student_id = Column(String, ForeignKey("User.student_id"), nullable=False, primary_key=True)
    room_id = Column(String, ForeignKey("Room.room_id"), nullable=False, primary_key=True)
    entered_at = Column(DateTime, server_default=func.now())


    # Relationship - total 2
    userroom_with_room = relationship("Room", back_populates="room_with_userroom")
    userroom_with_user = relationship("User", back_populates="user_with_userroom")