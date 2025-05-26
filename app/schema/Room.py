from pydantic import BaseModel

#NOTE: - 필드 추가 가능성 있음
class Room(BaseModel):
    room_id: str
    name: str
    is_available: bool = False
    
    class Config:
        orm_mode = True