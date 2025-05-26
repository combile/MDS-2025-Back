from sqlalchemy import Column, String, Boolean, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from enum import Enum

class Status(str, Enum):
    bad = "bad"
    medium = "medium"
    good = "good"
    

class Room(Base):
    __tablename__ = "Room"
    
    room_id = Column(String,primary_key=True, nullable=False)
    building_id = Column(String, ForeignKey("Building.building_id"),nullable=False)
    name = Column(String)
    floor = Column(Integer)
    is_available = Column(Boolean, server_default="false") #NOTE: SQL에서 "false"로 표기
    status = Column(Enum(Status, name="status_enum", create_type=False))
    
    #Relationship - total 5
    #Room <-> User 조인 테이블이 2개임
    room_fav_user = relationship("User", secondary="FavoriteRoom", back_populates="user_fav_room")
    room_with_favoriteroom = relationship("FavoriteRoom", back_populates="favoriteroom_with_room") #join table
    
    room_userroom_user = relationship("User", secondary="UserRoom", back_populates="user_userroom_room") 
    room_with_userroom = relationship("UserRoom", back_populates="userroom_with_room") #join table
    

    room_with_roomcondition = relationship("RoomCondition", back_populates="roomcondition_with_room")
    
    
    
    room_log_roomcondition = relationship("RoomCondition", secondary="AbnormalDataLog", back_populates="roomcondition_log_room")
    room_with_abnormaldatalog = relationship("AbnormalDataLog", back_populates="abnormaldatalog_with_room") #join table
    
    room_with_building = relationship("Building", back_populates="building_with_room")
    
    
    
    