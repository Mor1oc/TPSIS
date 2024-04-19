from sqlalchemy.orm import Session

from app.database.base import inject
from app.models import Carrier


@inject
def all_carriers(db: Session):
    return db.query(Carrier).all()
