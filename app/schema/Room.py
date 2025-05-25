from pydantic import BaseModel


class Room(BaseModel):
    room_id: str
    name: str
    is_available: bool = False
    
    class Config:
        orm_mode = True