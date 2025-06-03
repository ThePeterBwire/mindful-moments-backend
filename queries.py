from datetime import datetime
from sqlalchemy.orm import Session
from models import User, Journal, Quote, UserQuote

# User operations
def create_user(db: Session, username: str):
    db_user = User(username=username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Journal operations
def create_journal_entry(db: Session, user_id: int, mood: str, reflection: str):
    db_entry = Journal(
        user_id=user_id,
        mood=mood,
        reflection=reflection
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def get_user_entries(db: Session, user_id: int, mood_filter: str = None):
    query = db.query(Journal).filter(Journal.user_id == user_id)
    if mood_filter:
        query = query.filter(Journal.mood == mood_filter)
    return query.order_by(Journal.date.desc()).all()

# Quote operations
def create_quote(db: Session, text: str, author: str = None):
    db_quote = Quote(text=text, author=author)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote

def add_user_quote(db: Session, user_id: int, quote_id: int):
    db_user_quote = UserQuote(user_id=user_id, quote_id=quote_id)
    db.add(db_user_quote)
    db.commit()
    db.refresh(db_user_quote)
    return db_user_quote

def get_user_favorite_quotes(db: Session, user_id: int):
    return db.query(UserQuote).filter(UserQuote.user_id == user_id).order_by(UserQuote.date.desc()).all()