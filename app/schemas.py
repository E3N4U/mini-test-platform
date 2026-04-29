from pydantic import BaseModel

class APICreate(BaseModel):
    name: str
    url: str
    method: str


class CaseCreate(BaseModel):
    api_id: int
    input_data: str
    expected: str