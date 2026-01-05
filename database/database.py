from sqlite3 import connect
from tables import create_users_table, create_reels_table, create_user_reels_table

def connect_to_database():
    connection = connect("storage.db")
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    return connection, cursor

def initialize_tables():
    create_users_table()
    create_reels_table()
    create_user_reels_table()

if __name__ == "__main__":
    initialize_tables()
