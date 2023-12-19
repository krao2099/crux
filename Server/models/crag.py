from base import base

class crag(base):
    
    def __init__(self, id, date, name, state, coordinates, description, image, rating, user, published=False):
        super().__init__(id,date)
        self.set_name(name)
        self.set_state(state)
        self.set_coordinates(coordinates)
        self.set_description(description)
        self.set_image(image)
        self.set_rating(rating)
        self.set_user(user)
        self.set_published(published)


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

    def set_published(self, published):
        self.published = published

    def set_rating(self, rating):
        self.rating = rating

    def set_user(self, user):
        self.user = user

    def create_crag(self):
        pass

    def edit_crag(cragId, name, coordinates, description, image):
        pass

    def published_crag(cragId):
        pass

    def get_all_crags_pins():
        pass

    def get_crags_state(state):
        pass

    def get_historical(cragId):
        pass