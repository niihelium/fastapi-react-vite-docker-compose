from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
import sqlalchemy

from sqlalchemy.orm import Session
from . import crud, models, schemas

from .database import SessionLocal, engine

app = FastAPI()

origins = ["http://localhost:8080", "localhost:8080", "http://localhost", "localhost"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/")
async def root():
    return {"message": "Hello World!"}

@app.get("/api/greet")
async def get_greeting(db: Session = Depends(get_db)):
    return crud.get_greeting(db)