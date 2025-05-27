from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.requests import Request as FastAPIRequest
from sqlalchemy.orm import Session
from app.database import get_db
from app.model import User
from app.schema.User import UserSignUp



app = APIRouter()





@app.post("/api/users/signup")
async def sign_up(request : UserSignUp, db: Session=Depends(get_db)):
    
    if db.query(User).filter((User.id == request.id) | (User.student_id == request.student_id)).first():
        raise HTTPException(
            status_code = 409,
            detail="User already exists"
        )
        
    #User(entity) 생성 : DB에 저장
    #left: 컬럼 / right: pydantic 모델 필드
    new_user = User(
        student_id=request.student_id,
        id=request.id,
        password = request.password, #FIXME: 해싱처리 필요
        department=request.department,
        phone=request.phone_number,
        email=request.email,
        profile_photo=request.profile_photo
    )
    
    #레코드 저장
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message":"Sign up successful"}
    
    
    
    
    
    
    