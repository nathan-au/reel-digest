from app.bot import initialize_bot
from database.tables import initialize_tables

if __name__ == "__main__":
    initialize_tables()
    initialize_bot()