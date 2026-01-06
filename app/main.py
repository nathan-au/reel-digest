from app.bot import initialize_bot
from data.models import initialize_tables

if __name__ == "__main__":
    initialize_tables()
    initialize_bot()