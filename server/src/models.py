from .database import Base
from sqlalchemy import Column, Integer, String


class Greeting(Base):
    __tablename__ = "greetings"
    id = Column(Integer, primary_key=True)
    username = Column(String(255))