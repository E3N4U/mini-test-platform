from fastapi import FastAPI
from .database import Base, engine
from .routers import api_router, case_router, run_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router.router)
app.include_router(case_router.router)
app.include_router(run_router.router)