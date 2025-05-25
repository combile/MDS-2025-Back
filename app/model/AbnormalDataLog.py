from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class AbnormalDataLog(Base):
    __tablename__ = "AbnormalDataLog"
    
    log_id = Column(String, primary_key=True)
    room_id = Column(String)
    condition_id = Column(String, ForeignKey("RoomCondition.condition_id"))
    issue_type = Column(String, ForeignKey("Room.room_id"))
    message = Column(String)
    logged_at = Column(DateTime) #TimeStamp
    
    
    log_with_condition = relationship("RoomCondition", back_populates="room_condition_with_log")
    