import db

class Comment():
    
    def __init__(self, id, date, user, owner, text, beta):
        self.set_id(id)
        self.set_date(date)
        self.set_user(user) #fK to user
        self.set_owner(owner) #fk to either crag, wall, or route
        self.set_text(text)
        self.set_beta(beta)

    def set_id(self, id):
        self.id = id

    def set_date(self, date):
        self.date = date

    def set_user(self, user):
        self.user = user

    def set_owner(self, owner):
        self.owner = owner

    def set_text(self, text):
        self.text = text

    def set_beta(self, beta):
        self.beta = beta

    def get_betas(route_id):
        query = """SELECT * FROM RouteComments WHERE route_id = %s AND beta = TRUE"""
        params = (route_id)
        try:
            return db.execute(query, params, retrieve=True)
        except Exception as e:
            raise e

    def get_comments_wall(wall_id):
        query = """SELECT * FROM RouteComments JOIN Routes ON RouteComments.route_id = Routes.id WHERE wall_id = %s"""
        params = (wall_id)
        try:
            return db.execute(query, params, retrieve=True)
        except Exception as e:
            raise e

    def get_comments_route(route_id):
        pass

    def get_comments_crag(crag_id):
        query = """SELECT * FROM Walls AS W 
        
                    JOIN
        
                    (SELECT * FROM RouteComments JOIN Routes ON RouteComments.route_id = Routes.id) R

                    ON W.id = R.wall_id
        
                    WHERE crag_id = %s"""
        params = (crag_id)
        try:
            return db.execute(query, params, retrieve=True)
        except Exception as e:
            raise e