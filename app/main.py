from app.bot import initialize_bot
from database.database import initialize_all_tables

if __name__ == "__main__":
    initialize_all_tables()
    initialize_bot()