from sqlalchemy.orm import Session
from app.domain.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRepository:
    @staticmethod
    def get_user_by_username(db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def create_user(db: Session, username: str, password: str, role: str = "customer"):
        hashed_password = pwd_context.hash(password) 
        new_user = User(username=username, hashed_password=hashed_password, role=role)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
