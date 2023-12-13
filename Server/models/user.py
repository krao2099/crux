class User:
    def __init__(self, user_name, email, hash_pass):
        self.set_user_name(user_name)
        self.set_email(email)
        self.set_hash_pass(hash_pass)
        self.admin = False

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_email(self, email):
        self.email = email

    def set_hash_pass(self, hash_pass):
        self.hash_pass = hash_pass