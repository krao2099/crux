import db

def is_admin(user_id):
    query = """SELECT admin_flag FROM Users WHERE id = %s"""
    try:
        result = db.retrieve(query, (user_id,))
        return result[0][0]
    except Exception as e:
        return False