from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request as FastAPIRequest
from sqlalchemy.orm import Session
from app.database import get_db
from app.model import User #SQLAlchemy 모델
from app.schema.User import UserProfile #pydantic 모델

app = APIRouter()

#MARK: - 커스텀 예외 핸들러
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: FastAPIRequest, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error":exc.detail}
    )
    
@app.get("/api/users/{student_id}")
async def get_user_profile(student_id: str, db: Session=Depends(get_db)):
    
    user = db.query(User).filter(User.student_id == student_id).firts()
    
    if not user:
        raise HTTPException(
            status_code=500,
            detail="Server error"
        )
    
    #pydantic 모델로 변환
    #left: pydantic 모델 필드 / right: SQLAlchemy 모델 컬럼
    user_profile = UserProfile(
        student_id=user.student_id,
        id=user.id,
        name=user.name,
        department=user.department,
        phone_number=user.phone,
        email=user.email,
        profile_photo=user.profile_photo
    )
    
    return user_profile