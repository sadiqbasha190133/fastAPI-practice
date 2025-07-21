from sqlalchemy import Column, Integer, String
from database import Base

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    body = Column(String(500), nullable=False)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))