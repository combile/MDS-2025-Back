from pydantic import BaseModel

class FavoriteBuildingRequest(BaseModel):
    student_id: str
    building_id: str
    
    
class FavoriteRoomRequest(BaseModel):
    student_id: str
    building_id: str
    room_id: str