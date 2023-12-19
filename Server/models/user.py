from base import base

class User(base):
    def __init__(self, id, date, user_name, email, hash_pass, loginAttempts, ttl, admin=False):
        super().__init__(id,date)
        self.set_user_name(user_name)
        self.set_email(email)
        self.set_hash_pass(hash_pass)
        self.set_loginAttempts(loginAttempts)
        self.set_ttl(ttl)
        self.set_admin(admin)

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_email(self, email):
        self.email = email

    def set_hash_pass(self, hash_pass):
        self.hash_pass = hash_pass

    def set_loginAttempts(self, loginAttempts):
        self.loginAttempts = loginAttempts

    def set_ttl(self, ttl):
        self.ttl = ttl

    def set_admin(self, admin):
        self.admin = admin

    def create_user(self):
        pass
    
    def login_in_user(username, password):
        pass