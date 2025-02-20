from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import orders, auth
from app.core.config import settings
from app.infrastructure.db.base import init_db

import app.infrastructure.db.base_models  

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer()

init_db()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

@app.get("/")
def root():
    return {"message": "Welcome to the Order Management Service"}
