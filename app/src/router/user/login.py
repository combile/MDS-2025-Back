from fastapi import APIRouter, HTTPException, Depends, Request, status
from fastapi.responses import JSONResponse
from fastapi.requests import Request as FastAPIRequest
from sqlalchemy.orm import Session
from app.schema.User import UserLogin
from app.database import get_db
from app.model import User

app = APIRouter()

#MARK: - 커스텀 예외 핸들러
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: FastAPIRequest, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error":exc.detail}
    )
    

@app.post("/api/users/login")
async def login(request: UserLogin, db: Session = Depends(get_db)):
    
    user_id = request.id
    password = request.password
    
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





# from fastapi import APIRouter, HTTPException, status, Request, Depends
# from sqlalchemy.orm import Session
# from app.src.database import get_db
# from app.model import User  # User 모델이 정의되어 있다고 가정

# app = APIRouter()

# @app.post("/api/users/signup", status_code=201)
# async def sign_up(request: Request, db: Session = Depends(get_db)):
#     data = await request.json()
#     user_name = data.get("user_name")
#     student_id = data.get("student_id")
#     user_id = data.get("id")
#     password = data.get("password")
#     password_check = data.get("password_check")
#     email = data.get("email")
#     phone_number = data.get("phone_number")
#     consent = data.get("consent")
#     role = data.get("role")
#     profile_photo = data.get("profile_photo")

#     # 비밀번호 확인
#     if password != password_check:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Passwords do not match"
#         )

#     # ID 또는 학번 중복 확인
#     if db.query(User).filter((User.id == user_id) | (User.student_id == student_id)).first():
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail="ID or student_id already exists"
#         )

#     # User 생성 및 저장
#     new_user = User(
#         user_name=user_name,
#         student_id=student_id,
#         id=user_id,
#         password=password,  # 실제 서비스에서는 해시 사용 권장
#         email=email,
#         phone_number=phone_number,
#         consent=consent,
#         role=role,
#         profile_photo=profile_photo
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return {"message": "SignUp success"}