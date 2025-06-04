import argparse
from datetime import datetime
from database import SessionLocal
from models import User, Journal, Quote, UserQuote
import sys
from pyfiglet import Figlet
from termcolor import colored

# Install required packages: pip install pyfiglet termcolor

def display_banner():
    f = Figlet(font='slant')
    print(colored(f.renderText('Mindful Moments'), 'cyan'))
    print(colored("Your personal journaling companion\n", 'yellow'))

def main_menu():
    display_banner()
    print(colored("MAIN MENU", 'green', attrs=['bold']))
    print("1. User Management")
    print("2. Journal Entries")
    print("3. Quotes")
    print("4. View Statistics")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    return choice

def user_management():
    while True:
        print("\n" + colored("USER MANAGEMENT", 'green', attrs=['bold']))
        print("1. Create User")
        print("2. List Users")
        print("3. Back to Main Menu")
        
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            username = input("Enter username: ")
            with SessionLocal() as db:
                user = User(username=username)
                db.add(user)
                db.commit()
                print(colored(f"User created with ID: {user.id}", 'green'))
                
        elif choice == '2':
            with SessionLocal() as db:
                users = db.query(User).all()
                for user in users:
                    print(f"ID: {user.id} | Username: {user.username}")
        
        elif choice == '3':
            return
        else:
            print(colored("Invalid choice!", 'red'))

# Similar functions for journal_entries(), quotes_management(), show_stats()

if __name__ == "__main__":
    while True:
        try:
            choice = main_menu()
            
            if choice == '1':
                user_management()
            elif choice == '2':
                journal_entries()
            elif choice == '3':
                quotes_management()
            elif choice == '4':
                show_stats()
            elif choice == '5':
                print(colored("\nGoodbye! Keep being mindful!\n", 'yellow'))
                sys.exit()
            else:
                print(colored("Invalid choice! Try again.", 'red'))
                
        except KeyboardInterrupt:
            print(colored("\n\nExiting gracefully...", 'yellow'))
            sys.exit()