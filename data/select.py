from data.connect import connect_to_database

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