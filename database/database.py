from sqlite3 import connect

def connect_to_database():
    connection = connect("database/storage.db")
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    return connection, cursor