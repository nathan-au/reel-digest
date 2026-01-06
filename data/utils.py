from data.connect import connect_to_database

def print_tables():
    tables = ["users", "reels", "user_reels"]

    connection, cursor = connect_to_database()

    for table in tables:
        cursor.execute("SELECT * FROM " + table)
        rows = cursor.fetchall()
        print(table + " (" + str(len(rows)) + "):")
        if rows:
            for row in rows:
                print(row)
        else:
            print(table + " is empty.")
        print("")

    connection.close()

def print_total_duration():
    connection, cursor = connect_to_database()
    cursor.execute("SELECT SUM(duration) FROM reels")
    total_duration = cursor.fetchone()[0]
    connection.close()

    if total_duration is None:
        total_duration = 0

    duration_minutes = int(total_duration // 60)
    duration_seconds = int(total_duration % 60)

    print("Total Duration: " + str(duration_minutes) + " minutes and " + str(duration_seconds) + " seconds.\n")

if __name__ == "__main__":
    # print_tables()
    print_total_duration()