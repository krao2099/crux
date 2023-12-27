import db
import crux_utils

class Crag():
    
    def __init__(self, id, date, name, state, coordinates, description, image, rating, user):
        self.set_id(id)
        self.set_date(date)
        self.set_name(name)
        self.set_state(state)
        self.set_coordinates(coordinates)
        self.set_description(description)
        self.set_image(image)
        self.set_rating(rating)
        self.set_user(user)

    def set_id(self, id):
        self.id = id

    def set_date(self, date):
        self.date = date

    def set_name(self, name):
        self.name = name

    def set_state(self, state):
        self.state = state
    
    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def set_description(self, description):
        self.description = description

    def set_image(self, image):
        self.image = image

    def set_rating(self, rating):
        self.rating = rating

    def set_user(self, user):
        self.user = user

    def create_crag(self):
        query = """INSERT INTO Crags (name, creation_date, state, coordinates, 
                                        description, image_path, rating, 
                                        user_id) VALUES (%s, %s, %s, %s, 
                                                        %s, %s, %s, %s) RETURNING id"""
        record = (self.name, self.date, self.state, 
                  self.coordinates, self.description, self.image, 
                  self.rating, self.user)
        
        try:
            self.set_id(db.execute(query, record, retrieve=True))
        except Exception as e: 
            raise e

#Procedure needed, wait
def view_crag(user_id, crag_id):
    pass

def publish_crag(user_id, crag_id):

    if(not crux_utils.is_admin(user_id)):
        raise PermissionError("admin privelages required for publishing")
    query = """UPDATE Crags SET published = TRUE WHERE id = %s"""
    params = (crag_id,)
    try:
        db.execute(query, params)
    except Exception as e: 
        raise e

def get_all_unpublish_crags():
    query = """SELECT * FROM Crags WHERE published = FALSE"""
    try:
        return db.retrieve(query, None)
    except Exception as e:
        raise e

def get_my_unpublish_crags(user_id):
    query = """SELECT * FROM Crags WHERE published = FALSE AND user_id = %s"""
    params = (user_id)
    try:
        return db.retrieve(query, params)
    except Exception as e:
        raise e

#wait on this one
def get_all_crags__by_pins():
    pass

def get_crags_by_state(state):
    query = """SELECT * FROM Crags WHERE published = TRUE AND state = %s"""
    params = (state)
    try:
        return db.retrieve(query, params)
    except Exception as e:
        raise e

def get_historical(crag_id):
    query = """SELECT * FROM CragsHistorical WHERE crag_id = %s ORDER BY version_number DESC"""
    params = (crag_id)
    try:
        return db.retrieve(query, params)
    except Exception as e:
        raise e