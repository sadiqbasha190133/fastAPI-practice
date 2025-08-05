from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    body = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("Users", back_populates="blogs")


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))
    blogs = relationship("Blog", back_populates="creator")  # FIXED HERE


 