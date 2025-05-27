from sqlalchemy import Column, Enum as SQLEnum, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
from enum import Enum
# from app.model.User import User
# from app.model.RoomCondition import RoomCondition

class VoteEnum(str, Enum):
    cold = "cold"
    hot = "hot"
    ok = "ok"

class CurrentFeedBack(Base):
    __tablename__ = "CurrentFeedback"
    
    student_id = Column(String, ForeignKey("User.student_id"), nullable=False, primary_key=True)
    room_id = Column(String, ForeignKey("RoomCondition.room_id"), nullable=False)
    feedback_id = Column(String, nullable=False)
    vote = Column(SQLEnum(VoteEnum, name="vote_enum", create_type=False))
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    #Relationship - total 2
    currentfeedback_with_user = relationship("User", back_populates="user_with_currentfeedback")
    currentfeedback_with_roomcondition = relationship("RoomCondition", back_populates="roomcondition_with_currentfeedback")