from fastapi import APIRouter, HTTPException, Depends, Request, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model import User

app = APIRouter()

@app.post("/api/users/slogin")
async def login(request: Request, db: Session = Depends(get_db)):
    data = await request.json() #request 에서 json 추출
    
    #사용자 입력 정보
    user_id = data.get("id")
    password = data.get("password")
    
    #id 매칭
    user = db.query(User).filter(User.id == user_id).first()
    
    #사용자 존재 여부 확인
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not exist"
        )
        
    elif user and user.password != password:
        raise HTTPException(
            status_code = 401,
            detail="Invalid credentials"
        )
    
    return {"message": "Login successful"}





