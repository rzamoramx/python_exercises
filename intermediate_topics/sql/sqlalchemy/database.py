
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from intermediate_topics.sql.sqlalchemy.models.base import Base

engine = create_engine('sqlite:///:memory:')  # ('sqlite:///:memory:')  ('sqlite:///symbols.db')
session = sessionmaker(bind=engine)()


def create_db():
    Base.metadata.create_all(engine)


def get_session():
    return session
