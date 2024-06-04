
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from intermediate_topics.sql.sqlalchemy.models.base import Base

url_default = 'sqlite:///:memory:'  # ('sqlite:///:memory:')  ('sqlite:///symbols.db')
session = None
engine = None


def create_db(url=None):
    global engine

    if url:
        engine = create_engine(url)
    else:
        engine = create_engine(url_default)
    Base.metadata.create_all(engine)


def get_session():
    global session

    if session:
        return session

    return sessionmaker(bind=engine)()
