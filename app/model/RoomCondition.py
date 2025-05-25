from sqlalchemy import Column, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class RoomCondition(Base):
    condition_id = Column(String, primary_key=True)
    roomt_id = Column(String, ForeignKey("Room.room_id"), nullable=False)
    measured_at = Column(DateTime, server_default=func.now(),onupdate=func.now(),nullable=False)
    temperature = Column(Float)
    humidity = Column(Float)
    pm10 = Column(Float)
    pm25 = Column(Float)
    co2 = Column(Float)
    
    room_condition_with_log = relationship("AbnormalDataLog", back_populates="log_with_condition")
    room_condition_with_comment = relationship("AiComment", back_populates="comment_with_condition")
    