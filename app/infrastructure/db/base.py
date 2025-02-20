from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    """Функция для создания таблиц в базе данных"""
    from app.infrastructure.db.base_models import Base
    from app.infrastructure.db.base import engine
    Base.metadata.create_all(bind=engine)
