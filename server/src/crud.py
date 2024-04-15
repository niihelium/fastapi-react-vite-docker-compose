from sqlalchemy.orm import Session

from . import models, schemas

def get_greeting(db: Session) -> schemas.Greeting:
    return db.query(models.Greeting).first()