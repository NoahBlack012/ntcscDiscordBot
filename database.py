from email.policy import default
from enum import unique
import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

# Create base for database model
db = declarative_base()

class User(db):
    """
    Database to stores users
    Userid: Discord user id number
    Score: Integer to represent NT Spirit Score (Default value: 0)
    northle_plays: Number of times user has played northle
    total_northle_guesses: Total number of guesses made on northle
    northle_wins: Total number of times user has won on northle
    """
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    userid = Column(String, unique=True, nullable=False)
    score = Column(Integer, nullable=False, default=0)
    northle_plays = Column(Integer, nullable=False, default=0)
    total_northle_guesses = Column(Integer, nullable=False, default=0)
    northle_wins = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"{self.userid}, Score: {self.score}, Northle plays: {self.northle_plays}, Total Northle Guesses: {self.total_northle_guesses}, Northle Wins: {self.northle_wins}"

class Northle_Table(db):
    """
    Database to store info about the northle game
    Date: Date corresponding to current word
    Word: Current word
    Number: nth northle
    next_words: All of the next words separeted by commas
    users: ID's of users who have completed the day's northle
    """
    __tablename__ = "Northle"
    id = Column(Integer, primary_key=True)
    date = Column(String(), unique=True, nullable=False)
    word = Column(String(), unique=True, nullable=False)
    number = Column(Integer, nullable=False)
    next_words = Column(String(), nullable=False)
    users = Column(String(), nullable=False, default="")

    def __repr__(self):
        return f"{self.date}, {self.word}, {self.number}, [{self.next_words}]"

# Get database URI from environment variables
DATABASE_URI = os.environ["DATABASE_URI"]
if not DATABASE_URI:
    raise RuntimeError

# Create database engine
engine = create_engine(DATABASE_URI, echo=False)
