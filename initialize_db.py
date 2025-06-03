# initialize_db.py
from database import Base, engine
from models import User, Journal, Quote, UserQuote  # This is crucial!

def initialize_database():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    initialize_database()