import db
class User():
    def __init__(self, id, date, username, email, hash_password):
        self.set_id(id)
        self.set_date(date)
        self.set_username(username)
        self.set_email(email)
        self.set_hash_password(hash_password)

    def set_id(self, id):
        self.id = id

    def set_date(self, date):
        self.date = date

    def set_username(self, username):
        self.username = username

    def set_email(self, email):
        self.email = email

    def set_hash_password(self, hash_password):
        self.hash_password = hash_password


    def create_user(self):
        query = "INSERT INTO Users (username, email, hash_password) VALUES (%s, %s, %s) RETURNING id;"
        record = (self.username, self.email, self.hash_password)
        try:
            self.set_id(db.execute(query, record, retrieve=True))
        except Exception as e: 
            raise e
    
    def login_in_user(username, password):
        pass