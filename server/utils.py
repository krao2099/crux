import db

def is_admin(user_id):
    query = """SELECT * FROM Admins"""
    params = ()
    try:
        result = db.execute(query, params, retrieve=True)
        return user_id in result
    except Exception as e:
        raise e