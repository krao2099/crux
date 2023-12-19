import psycopg2

class user():
    def db_connect(self):
        return psycopg2.connect(host="localhost",dbname="crux_db", user="postgres", password="test1234")
    
    def __init__(self, id, date, username, email, hash_password, login_attempts, ttl, admin_flag=False):
        self.set_id = id
        self.set_creation_date = date
        self.set_username(username)
        self.set_email(email)
        self.set_hash_password(hash_password)
        self.set_login_attempts(login_attempts)
        self.set_ttl(ttl)
        self.set_admin_flag(admin_flag)

    def set_username(self, username):
        self.username = username

    def set_email(self, email):
        self.email = email

    def set_hash_password(self, hash_password):
        self.hash_password = hash_password

    def set_login_attempts(self, login_attempts):
        self.login_attempts = login_attempts

    def set_ttl(self, ttl):
        self.ttl = ttl

    def set_admin_flag(self, admin_flag):
        self.admin_flag = admin_flag
    
    def set_id(self, id):
        self.id = id

    def set_date(self, date):
        self.date = date

    def create_user(self):
        conn = self.db_connect()
        cursor = conn.cursor()

        query = """ INSERT INTO Users (username, email, hash_password) VALUES (%s, %s, %s)"""
        record = (self.username, self.email, self.hash_password)
        cursor.execute(query, record)
        conn.commit()
        conn.close()
        print("Success")
    
    def login_in_user(username, password):
        pass