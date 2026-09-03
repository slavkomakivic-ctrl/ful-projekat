from fastapi import FastAPI
import database  # pokreće CREATE TABLE kad se importuje
from routes import router as auth_router
from knjige_routes import router as knjige_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(knjige_router)