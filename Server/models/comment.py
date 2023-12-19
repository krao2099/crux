from base import base

class comment(base):
    
    def __init__(self, id, date, user, owner, text, beta):
        super().__init__(id,date)
        self.set_user(user) #fK to user
        self.set_owner(owner) #fk to either crag, wall, or route
        self.set_text(text)
        self.set_beta(beta)

    def set_user(self, user):
        self.user = user

    def set_owner(self, owner):
        self.owner = owner

    def set_text(self, text):
        self.text = text

    def set_beta(self, beta):
        self.beta = beta

    def get_betas(route_id):
        pass

    def get_comments_wall(wallId):
        pass

    def get_comments_route(routeId):
        pass

    def get_comments_crag(cragId):
        pass