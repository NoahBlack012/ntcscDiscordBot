import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

# Create base for database model
db = declarative_base()

class User(db):
    """
    Class to represent a user
    Name: String (Username obtained directly from discord, stored hashed)
    Score: Integer to represent NT Spirit Score (Default value: 0)
    """
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    name = Column(String(), unique=True, nullable=False)
    score = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"{self.name} has a score of {self.score}"

# Get database URI from environment variables
DATABASE_URI = os.environ["DATABASE_URI"]
if not DATABASE_URI:
    raise RuntimeError

# Create database engine
engine = create_engine(DATABASE_URI, echo=True)
