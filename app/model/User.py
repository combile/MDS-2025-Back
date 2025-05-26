from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "User"
    
    student_id = Column(String, primary_key=True, nullable=False)
    id = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    department = Column(String)
    phone = Column(String)
    email = Column(String)
    profile_photo = Column(String)
    consent = Column(Boolean)
    role = Column(String)
    
    # Relationship: - total 4
    user_favoritebuilding_building = relationship("Building", secondary="FavoriteBuilding", back_populates="building_favoritebuilding_user")
    user_with_favoritebuilding = relationship("FavoriteBuilding", back_populates="favoritebuilding_with_user") #join table
    
    user_fav_room= relationship("Room", secondary="FavoriteRoom", back_populates="room_fav_user")
    user_with_favoriteroom = relationship("FavoriteRoom", back_populates="favoriteroom_with_user") #join table
    
    user_userroom_room= relationship("Room", secondary="UserRoom", back_populates="room_userroom_user")
    user_with_userroom = relationship("UserRoom", back_populates="userroom_with_user") #join table
    
    
    user_currentfeedback_roomcondition = relationship("RoomCondition", secondary="CurrentFeedback", back_populates="roomcondition_currentfeedback_user")
    user_with_currentfeedback = relationship("CurrentFeedBack", back_populates="currentfeedback_with_user") #join table
    
    
    
    
    
    