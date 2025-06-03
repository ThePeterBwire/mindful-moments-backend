from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    journal_entries = relationship("Journal", back_populates="user")
    favorite_quotes = relationship("UserQuote", back_populates="user")

class Journal(Base):
    __tablename__ = 'journal'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    mood = Column(String(20), nullable=False)
    reflection = Column(Text, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="journal_entries")

class Quote(Base):
    __tablename__ = 'quotes'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(Text, nullable=False)
    author = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user_associations = relationship("UserQuote", back_populates="quote")

class UserQuote(Base):
    __tablename__ = 'user_quotes'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    quote_id = Column(Integer, ForeignKey('quotes.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="favorite_quotes")
    quote = relationship("Quote", back_populates="user_associations")