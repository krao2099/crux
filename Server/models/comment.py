from base import base

class comment(base):
    
    def __init__(self, id, date, user, owner, text):
        super().__init__(id,date)
        self.set_user(user) #fK to user
        self.set_owner(owner) #fk to either crag, wall, or route
        self.set_text(text)

    def set_user(self, user):
        self.user = user

    def set_owner(self, owner):
        self.owner = owner

    def set_text(self, text):
        self.text = text