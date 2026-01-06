from database.database import connect_to_database

def insert_user(id, first_name):
    connection, cursor = connect_to_database()
    cursor.execute("INSERT OR IGNORE INTO users (id, first_name) VALUES (?, ?)", (id, first_name))
    connection.commit()
    connection.close()

def insert_reel(id, url, summary, duration):
    connection, cursor = connect_to_database()
    cursor.execute("INSERT OR IGNORE INTO reels (id, url, summary, duration) VALUES (?, ?, ?, ?)", (id, url, summary, duration))
    connection.commit()
    connection.close()

def insert_user_reel(user_id, reel_id):
    connection, cursor = connect_to_database()
    cursor.execute("INSERT OR IGNORE INTO user_reels (user_id, reel_id) VALUES (?, ?)", (user_id, reel_id))
    connection.commit()
    connection.close()