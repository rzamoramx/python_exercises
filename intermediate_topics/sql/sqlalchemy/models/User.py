
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from intermediate_topics.sql.sqlalchemy.models.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    posts = relationship('Post', back_populates='author')  # backref='user', lazy=True)
