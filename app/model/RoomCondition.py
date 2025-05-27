from sqlalchemy import Column, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
# from app.model.Room import Room
# from app.model.AiComment import AiComment
# from app.model.AbnormalDataLog import AbnormalDataLog
# from app.model.CurrentFeedBack import CurrentFeedBack
# from app.model.User import User
class RoomCondition(Base):
    __tablename__ = "RoomCondition"
    
    condition_id = Column(String, primary_key=True)
    room_id = Column(String, ForeignKey("Room.room_id"), nullable=False)
    measured_at = Column(DateTime, server_default=func.now(),onupdate=func.now(),nullable=False)
    temperature = Column(Float)
    humidity = Column(Float)
    pm10 = Column(Float)
    pm25 = Column(Float)
    co2 = Column(Float)
    
    #Relationship - total 4
    roomcondition_log_room = relationship("Room", secondary="AbnormalDataLog", back_populates="room_log_roomcondition")
    roomcondition_with_log = relationship("AbnormalDataLog", back_populates="log_with_roomcondition") #join table
    
    roomcondition_with_room = relationship("Room", back_populates="room_with_roomcondition")
    
    roomcondition_with_comment = relationship("AiComment", back_populates="comment_with_roomcondition")
    
    roomcondition_currentfeedback_user = relationship("User", secondary="CurrentFeedback", back_populates="user_currentfeedback_roomcondition")
    roomcondition_with_currentfeedback = relationship("CurrentFeedBack", back_populates="currentfeedback_with_roomcondition") #join table
    
    
    
    
    
    