import sys
sys.path.append("../Server")
import db
import re
from werkzeug.security import generate_password_hash

USERNAME_REGEX = r'^[a-zA-Z0-9]*$'
EMAIL_REGEX = r'^\S+@\S+\.\S+$'
PASSWORD_REGEX = r'^^(?=.*[a-z])(?=.*[0-9])(?=.*\W).*$'

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
        if re.match(USERNAME_REGEX, username):
            self.username = username
        else:
            raise ValueError("Invalid Username pattern")

    def set_email(self, email):
        if re.match(EMAIL_REGEX, email):
            self.email = email
        else:
            raise ValueError("Invalid email pattern")

    def set_hash_password(self, password):
        if re.match(PASSWORD_REGEX, password):
            self.hash_password = generate_password_hash(password)
        else:
            raise ValueError("Invalid password pattern")


    def create_user(self):
        query = "INSERT INTO Users (username, email, hash_password) VALUES (%s, %s, %s) RETURNING id;"
        record = (self.username, self.email, self.hash_password)
        try:
            self.set_id(db.execute(query, record, retrieve=True))
        except Exception as e: 
            raise e
    
    @staticmethod
    def retrieve_hash_password(username):
        query = """SELECT retrieve_hash_password(%s)"""
        params = (username,)
        return db.retrieve(query, params)[0][0]

    @staticmethod
    def login_success(username):
        query = """SELECT login_success(%s)"""
        params = (username,)
        return db.retrieve(query, params)[0][0]