from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.infrastructure.db.database import get_db
from app.infrastructure.db.repository.user_repository import UserRepository
from app.domain.models.user import User

router = APIRouter()
security = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class RegisterRequest(BaseModel):
    username: str
    password: str
    role: str = "customer"

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = UserRepository.get_user_by_username(db, request.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = pwd_context.hash(request.password)
    new_user = User(username=request.username, hashed_password=hashed_password, role=request.role)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = UserRepository.get_user_by_username(db, request.username)
    if not user or not pwd_context.verify(request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"access_token": "your_token_here", "token_type": "bearer"}

@router.get("/protected")
def protected_route(token=Depends(security)):
    return {"message": "You are authorized", "token": token.credentials}
