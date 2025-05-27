from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
# from app.model.RoomCondition import RoomCondition
# from app.model.Room import Room

class AbnormalDataLog(Base):
    __tablename__ = "AbnormalDataLog"
    
    log_id = Column(String, primary_key=True)
    room_id = Column(String, ForeignKey("Room.room_id"))
    condition_id = Column(String, ForeignKey("RoomCondition.condition_id"))
    issue_type = Column(String)
    message = Column(String)
    logged_at = Column(DateTime) #TimeStamp
    
    # Relationship - total 2
    log_with_roomcondition = relationship("RoomCondition", back_populates="roomcondition_with_log")
    abnormaldatalog_with_room = relationship("Room", back_populates="room_with_abnormaldatalog")