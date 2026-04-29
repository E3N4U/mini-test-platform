from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/api/create")
def create_api(api: schemas.APICreate, db: Session = Depends(get_db)):
    return crud.create_api(db, api)


@router.get("/api/list")
def list_api(db: Session = Depends(get_db)):
    return crud.get_apis(db)