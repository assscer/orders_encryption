from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Order Service"
    PROJECT_VERSION: str = "1.0"
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
