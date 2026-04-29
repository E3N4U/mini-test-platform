from fastapi import APIRouter
from runner.runner import run_tests

router = APIRouter()

@router.get("/run")
def run():
    return run_tests()