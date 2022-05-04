from database import db, User, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select 

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

def new_user(userid):
    # Create a new user and add it to the database
    user = User(userid=userid) # Create new user object
    session.add(user) # Add user to session
    session.commit() # Commit to database

def user_exists(userid):
    # Check if a user exists
    user = session.execute(select(User).filter_by(userid=userid)).scalar() # Query users with given name
    return user is not None # Return if user given by name exists in database

def get_score(userid):
    user = session.execute(select(User).filter_by(userid=userid)).scalar() # Query users with given name
    return user # Return user object

def update_score(userid, score_change):
    user = session.execute(select(User).filter_by(userid=userid)).scalar() # Query users with given name
    user.score += score_change # Add score change to current score
    session.add(user) # Add user to session
    session.commit() # Commit to database