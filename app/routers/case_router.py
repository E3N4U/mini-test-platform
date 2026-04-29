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


@router.post("/case/create")
def create_case(case: schemas.CaseCreate, db: Session = Depends(get_db)):
    return crud.create_case(db, case)


@router.get("/case/list")
def list_case(db: Session = Depends(get_db)):
    return crud.get_cases(db)