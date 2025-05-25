from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class AiComment(Base):
    comment_id = Column(String, primary_key=True, nullable=False)
    condition_id = Column(String, ForeignKey("RoomCondition.condition_id"), nullable=False)
    comment_text = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    
    comment_with_condition = relationship("RoomCondition", back_populates="room_condition_with_comment")