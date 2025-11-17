from sqlmodel import SQLModel, Session, create_engine
from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    echo=False
)

def get_session():
    with Session(engine) as session:
        yield session