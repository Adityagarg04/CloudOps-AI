from uuid import uuid4

from sqlalchemy import select

from src.database import Base, SessionLocal, engine, init_db
from src.models import User


def unique_email(prefix: str) -> str:
    return f"{prefix}-{uuid4().hex[:8]}@example.com"


def test_database_connection_and_user_persistence():
    Base.metadata.create_all(bind=engine)

    email = unique_email("alice")
    session = SessionLocal()
    try:
        user = User(email=email, name="Alice")
        session.add(user)
        session.commit()
        session.refresh(user)

        saved_user = session.execute(select(User).where(User.email == email)).scalar_one()
        assert saved_user.id is not None
        assert saved_user.name == "Alice"
        assert saved_user.email == email
    finally:
        session.close()


def test_database_ignores_empty_email_validation_in_model_shape():
    email = unique_email("bob")
    session = SessionLocal()
    try:
        user = User(email=email, name="Bob")
        session.add(user)
        session.commit()
        session.refresh(user)

        saved_user = session.execute(select(User).where(User.email == email)).scalar_one()
        assert saved_user.email == email
        assert saved_user.name == "Bob"
    finally:
        session.close()


init_db()
