# models/user.py
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"   # this is the actual SQL table name

    id = Column(Integer, primary_key=True, index=True)
    # primary_key=True → SQLite auto-assigns id: 1, 2, 3, ...
    # index=True       → creates a B-tree index; lookups by id are O(log n)

    username = Column(String(50), unique=True, nullable=False)
    # unique=True    → two users cannot have the same username
    # nullable=False → every user must have a username

    hashed_password = Column(String, nullable=False)
    # We NEVER store plain text passwords — only the bcrypt hash