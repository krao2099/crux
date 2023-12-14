class User:
    def __init__(self, user_name, email, hash_pass, admin=False):
        self.set_user_name(user_name)
        self.set_email(email)
        self.set_hash_pass(hash_pass)
        self.set_admin(admin)

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_email(self, email):
        self.email = email

    def set_hash_pass(self, hash_pass):
        self.hash_pass = hash_pass

    def set_admin(self, admin):
        self.admin = admin