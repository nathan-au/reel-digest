from sqlite3 import connect
from core.constants import PATH_TO_DATABASE

def connect_to_database():
    connection = connect(PATH_TO_DATABASE)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    return connection, cursor