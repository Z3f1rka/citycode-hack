from pydantic import BaseModel, ConfigDict

class TestCreate(BaseModel):
    text: str

class TestReturn(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    text: str