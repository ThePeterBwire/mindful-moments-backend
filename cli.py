import argparse
from datetime import datetime
from queries import (
    create_user, create_journal_entry, get_user_entries,
    create_quote, add_user_quote, get_user_favorite_quotes
)
from database import SessionLocal

def main():
    parser = argparse.ArgumentParser(description="Mindful Moments Journal CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    # User commands
    user_parser = subparsers.add_parser("user", help="User operations")
    user_parser.add_argument("--create", help="Create a new user", type=str)
    
    # Journal commands
    journal_parser = subparsers.add_parser("journal", help="Journal operations")
    journal_parser.add_argument("--add", action="store_true", help="Add a new entry")
    journal_parser.add_argument("--user", type=int, required=True, help="User ID")
    journal_parser.add_argument("--mood", choices=["happy", "neutral", "sad"], help="Mood for new entry")
    journal_parser.add_argument("--text", help="Reflection text for new entry")
    journal_parser.add_argument("--list", action="store_true", help="List all entries")
    journal_parser.add_argument("--filter", choices=["happy", "neutral", "sad"], help="Filter entries by mood")
    
    # Quote commands
    quote_parser = subparsers.add_parser("quote", help="Quote operations")
    quote_parser.add_argument("--add", action="store_true", help="Add a new quote")
    quote_parser.add_argument("--text", help="Quote text")
    quote_parser.add_argument("--author", help="Quote author")
    quote_parser.add_argument("--favorite", action="store_true", help="Favorite a quote")
    quote_parser.add_argument("--user", type=int, help="User ID for favorite")
    quote_parser.add_argument("--quote-id", type=int, help="Quote ID to favorite")
    quote_parser.add_argument("--list-favorites", action="store_true", help="List favorite quotes")
    
    args = parser.parse_args()
    db = SessionLocal()
    
    try:
        if args.command == "user" and args.create:
            user = create_user(db, args.create)
            print(f"Created user: ID {user.id}, Username {user.username}")
        
        elif args.command == "journal":
            if args.add:
                if not args.mood or not args.text:
                    print("Error: Both --mood and --text are required for adding an entry")
                    return
                entry = create_journal_entry(db, args.user, args.mood, args.text)
                print(f"Added journal entry: ID {entry.id}")
            
            elif args.list:
                entries = get_user_entries(db, args.user, args.filter)
                for entry in entries:
                    print(f"\nID: {entry.id}")
                    print(f"Mood: {entry.mood}")
                    print(f"Date: {entry.date}")
                    print(f"Reflection: {entry.reflection}")
        
        elif args.command == "quote":
            if args.add:
                if not args.text:
                    print("Error: --text is required for adding a quote")
                    return
                quote = create_quote(db, args.text, args.author)
                print(f"Added quote: ID {quote.id}")
            
            elif args.favorite:
                if not args.user or not args.quote_id:
                    print("Error: Both --user and --quote-id are required for favoriting")
                    return
                user_quote = add_user_quote(db, args.user, args.quote_id)
                print(f"Added favorite quote: ID {user_quote.id}")
            
            elif args.list_favorites:
                if not args.user:
                    print("Error: --user is required for listing favorites")
                    return
                favorites = get_user_favorite_quotes(db, args.user)
                for fav in favorites:
                    print(f"\nFavorite ID: {fav.id}")
                    print(f"Quote: {fav.quote.text}")
                    print(f"Author: {fav.quote.author}")
                    print(f"Date Favorited: {fav.date}")
    
    finally:
        db.close()

if __name__ == "__main__":
    main()