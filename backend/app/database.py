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

"""
SQLModel - base class for models
Session - represents a database session/connection.
    used to query, add, update or delete data
create_engine - created an SQLAlchemy engine, which manages connection to database
settings - holds database url

echo=False - if true, SQLAlchemy prints every SQL query executed to the console

get_session() - dependency generator for fastapi
    with Session(engine) as session - opens a database session using the engine
    context manager ensures session is closed automatically after use
    
    yield session - generator function, used by fastapi's Depends

when a request hits an endpoint:
    fastapi calls get_session(),
    provides session object to endpoint
    closes session after request finishes
"""