
from pydantic import BaseModel

class GreetingBase(BaseModel):
    username: str

class GreetingCreate(GreetingBase):
    pass

class Greeting(GreetingBase):
    id: int