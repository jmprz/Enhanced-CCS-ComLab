from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, change this to your specific URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# This line creates the tables in Postgres if they don't exist
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"status": "Database Connected & Tables Created"}

@app.post("/register", response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    db_user = db.query(models.User).filter(models.User.student_id == user.student_id).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Student ID already registered")
    
    # Create new user
    new_user = models.User(
        student_id=user.student_id,
        full_name=user.full_name,
        role=user.role,
        password_hash=user.password # Note: We will add hashing later!
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login")
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    # 1. Find the user by student_id
    user = db.query(models.User).filter(models.User.student_id == user_credentials.student_id).first()
    
    # 2. If user doesn't exist
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # 3. Check if password matches (We'll use verify_password here later)
    if user.password_hash != user_credentials.password:
        raise HTTPException(status_code=401, detail="Invalid password")
    
    return {"message": "Login successful", "role": user.role}