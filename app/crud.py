from sqlalchemy.orm import Session
from . import models, schemas

def create_api(db: Session, api: schemas.APICreate):
    db_api = models.API(**api.dict())
    db.add(db_api)
    db.commit()
    db.refresh(db_api)
    return db_api


def get_apis(db: Session):
    return db.query(models.API).all()


def create_case(db: Session, case: schemas.CaseCreate):
    db_case = models.TestCase(**case.dict())
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case


def get_cases(db: Session):
    return db.query(models.TestCase).all()