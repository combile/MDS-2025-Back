from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
# from app.model.RoomCondition import RoomCondition

class AiComment(Base):
    __tablename__ = "AiComment"
    
    comment_id = Column(String, primary_key=True, nullable=False)
    condition_id = Column(String, ForeignKey("RoomCondition.condition_id"), nullable=False)
    comment_text = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    
    #Relationship - total 1
    comment_with_roomcondition = relationship("RoomCondition", back_populates="roomcondition_with_comment")