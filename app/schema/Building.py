from pydantic import BaseModel

#MARK: - 단일 건물 정보 표현 모델
class Building(BaseModel):
    building_code: str
    name: str
    is_available: bool = False #기본값 설치
    
    
