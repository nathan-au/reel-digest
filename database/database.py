from sqlite3 import connect
from core.constants import DATABASE_PATH

def connect_to_database():
    connection = connect(DATABASE_PATH)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    return connection, cursor

def create_users_table():
    connection, cursor = connect_to_database()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, first_name TEXT)")
    connection.commit()
    connection.close()

def create_reels_table():
    connection, cursor = connect_to_database()
    cursor.execute("CREATE TABLE IF NOT EXISTS reels (id TEXT PRIMARY KEY, url TEXT, summary TEXT, duration REAL)")   
    connection.commit()
    connection.close()

def create_user_reels_table():
    connection, cursor = connect_to_database()
    cursor.execute("CREATE TABLE IF NOT EXISTS user_reels (user_id INTEGER, reel_id TEXT, created_at  DATETIME DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (user_id, reel_id), FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (reel_id) REFERENCES reels(id))")
    connection.commit()
    connection.close()

def initialize_all_tables():
    create_users_table()
    create_reels_table()
    create_user_reels_table()

if __name__ == "__main__":
    initialize_all_tables()