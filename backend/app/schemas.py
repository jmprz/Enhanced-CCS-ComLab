from pydantic import BaseModel
from typing import Optional

# To handle student/teacher registration
class UserCreate(BaseModel):
    student_id: str
    full_name: str
    password: str
    role: str # 'Admin', 'Teacher', or 'Student'

# To send user data back to the Frontend (without the password)
class UserOut(BaseModel):
    id: int
    student_id: str
    full_name: str
    role: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    student_id: str
    password: str