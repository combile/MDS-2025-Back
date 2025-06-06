from pydantic import BaseModel, EmailStr, root_validator



class UserSignUp(BaseModel):
    user_name: str
    student_id: str
    id: str
    password: str
    password_check: str #NOTE: DB 저장 X , 검증용으로만 사용
    email: EmailStr
    phone_number: str
    role: str
    profile_photo: str | None
    
    @root_validator()
    def check_password_match(cls, values):
        pw = values.get("password")
        pw_check = values.get("password_check")
        
        #비밀번호 다른 경우 
        if pw != pw_check:
            raise ValueError("Passwords do not match")
        return values
    

class UserLogin(BaseModel):
    id: str
    password: str
    
class UserProfile(BaseModel):
    student_id: str
    id: str
    name: str
    department: str
    phone_number: str
    email: EmailStr
    profile_photo: str | None #Optional[str]과 동일 / NULL 허용