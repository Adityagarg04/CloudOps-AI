from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.models import User


def create_user(db: Session, name: str, email: str) -> User:
    user = User(name=name, email=email)
    db.add(user)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise ValueError("A user with this email already exists.") from exc
    db.refresh(user)
    return user


def list_users(db: Session):
    return db.execute(select(User).order_by(User.id)).scalars().all()


def get_user_by_id(db: Session, user_id: int):
    return db.get(User, user_id)
