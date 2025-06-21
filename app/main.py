from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import init_db, SessionLocal
from .models import RadioShow
from .schemas import RadioShowCreate, RadioShowOut
from typing import List

app = FastAPI()

# Initialize the database and create tables
init_db()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the MCB Archives Backend!"}

@app.get("/shows", response_model=List[RadioShowOut])
def list_shows(db: Session = Depends(get_db)):
    return db.query(RadioShow).all()

@app.post("/shows", response_model=RadioShowOut)
def create_show(show: RadioShowCreate, db: Session = Depends(get_db)):
    db_show = RadioShow(**show.dict())
    db.add(db_show)
    db.commit()
    db.refresh(db_show)
    return db_show
