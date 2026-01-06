from database.database import connect_to_database

def select_all_users():
    connection, cursor = connect_to_database()
    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()
    connection.close()
    return all_users

def select_all_reels():
    connection, cursor = connect_to_database()
    cursor.execute("SELECT * FROM reels")
    all_reels = cursor.fetchall()
    connection.close()
    return all_reels

def select_all_user_reels():
    connection, cursor = connect_to_database()
    cursor.execute("SELECT * FROM user_reels")
    all_user_reels = cursor.fetchall()
    connection.close()
    return all_user_reels

def select_recent(user_id):
    connection, cursor = connect_to_database()
    cursor.execute(
        """
        SELECT reels.url, user_reels.created_at, reels.summary
        FROM user_reels
        JOIN reels ON user_reels.reel_id = reels.id
        WHERE user_reels.user_id = ?
        ORDER BY user_reels.created_at DESC
        LIMIT 5
        """,
        (user_id,)
    )
    user_reels = cursor.fetchall()
    connection.close()
    return user_reels

def select_saved_summary(reel_id):
    connection, cursor = connect_to_database()
    cursor.execute("SELECT summary FROM reels WHERE id = ?", (reel_id,))
    reel_summary = cursor.fetchall()
    connection.close()
    if (reel_summary):
        return reel_summary[0]
    return None

def print_all_tables():
    all_users = select_all_users()
    all_reels = select_all_reels()
    all_user_reels = select_all_user_reels()

    print("\nALL USERS:")
    print(len(all_users))
    if all_users:
        for user in all_users:
            print(user)
    else:
        print("No users found.")

    print("\nALL REELS:")
    print(len(all_reels))
    if all_reels:
        for reel in all_reels:
            print(reel)
    else:
        print("No reels found.")
    
    print("\nALL USER_REELS:")
    print(len(all_user_reels))
    if all_user_reels:
        for user_reel in all_user_reels:
            print(user_reel)
    else:
        print("No user_reels found")
    
    print("")

if __name__ == "__main__":
    print_all_tables()