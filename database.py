import sqlite3

def initialize_database():
    create_users_table()
    create_reels_table()
    create_user_reels_table()

def connect_to_database():
    connection = sqlite3.connect("database.db")
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    return connection, cursor

# users

def create_users_table():
    connection, cursor = connect_to_database()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, first_name TEXT)")
    connection.commit()
    connection.close()

def insert_user(id, first_name):
    connection, cursor = connect_to_database()
    cursor.execute("INSERT OR IGNORE INTO users (id, first_name) VALUES (?, ?)", (id, first_name))
    connection.commit()
    connection.close()

def select_all_users():
    connection, cursor = connect_to_database()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)
    connection.close()

# reels

def create_reels_table():
    connection, cursor = connect_to_database()
    cursor.execute("CREATE TABLE IF NOT EXISTS reels (id TEXT PRIMARY KEY, url TEXT, extractor_key TEXT, duration REAL, thumbnail TEXT, transcript TEXT, summary TEXT)")   
    connection.commit()
    connection.close()

def insert_reel(id, url, extractor_key, duration, thumbnail, transcript, summary):
    connection, cursor = connect_to_database()
    cursor.execute("INSERT OR IGNORE INTO reels (id, url, extractor_key, duration, thumbnail, transcript, summary) VALUES (?, ?, ?, ?, ?, ?, ?)", (id, url, extractor_key, duration, thumbnail, transcript, summary))
    connection.commit()
    connection.close()

def select_all_reels():
    connection, cursor = connect_to_database()
    cursor.execute("SELECT * FROM reels")
    reels = cursor.fetchall()
    for reel in reels:
        print(reel)
    connection.close()

# user reels 

def create_user_reels_table():
    connection, cursor = connect_to_database()
    cursor.execute("CREATE TABLE IF NOT EXISTS user_reels (user_id INTEGER, reel_id TEXT, PRIMARY KEY (user_id, reel_id), FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (reel_id) REFERENCES reels(id))")
    connection.commit()
    connection.close()

def insert_user_reel(user_id, reel_id):
    connection, cursor = connect_to_database()
    cursor.execute("INSERT OR IGNORE INTO user_reels (user_id, reel_id) VALUES (?, ?)", (user_id, reel_id))
    connection.commit()
    connection.close()

def select_all_user_reels():
    connection, cursor = connect_to_database()
    cursor.execute("SELECT * FROM user_reels")
    user_reels = cursor.fetchall()
    for user_reel in user_reels:
        print(user_reel)
    connection.close()

def select_user_reels(user_id):
    connection, cursor = connect_to_database()
    cursor.execute("SELECT * FROM user_reels WHERE user_id = ?", (user_id,))
    user_reels = cursor.fetchall()
    connection.close()
    return user_reels


if __name__ == "__main__":
    initialize_database()
