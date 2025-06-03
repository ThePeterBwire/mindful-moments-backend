# Mindful Moments Journal 📔✨

A command-line journaling app to track daily moods, reflections, and favorite quotes, built with Python and SQLite.

![Demo GIF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDhyN2UydG5xY3B6Y2R0ZGJ6ZXV5Z2VjeHd2Z2h0eHdkYzN5bWZ6biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ohs4kI2X9hD3WQvLi/giphy.gif)

## Features 🌟
- ✍️ **Journal entries** with mood tracking (😊 Happy/😐 Neutral/😢 Sad)
- 💖 **Save inspirational quotes**
- 🔍 **Filter entries** by mood
- 📊 **SQLite database** for persistent storage
- 🖥️ **Easy CLI interface**

## Tech Stack 🛠️
| Component       | Technology |
|-----------------|------------|
| Backend         | Python 3.8+ |
| Database        | SQLite + SQLAlchemy ORM |
| CLI Framework   | argparse |
| Testing         | pytest (optional) |

## Installation 💻
```bash
# Clone repository
git clone https://github.com/yourusername/mindful-moments-journal.git
cd mindful-moments-journal

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
