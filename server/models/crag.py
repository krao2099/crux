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
        pass

    #wait on this one
    def edit_crag(cragId, name, coordinates, description, image):
        pass

    #Procedure needed, wait
    def view_crag(userId, cragId):
        pass

    def publish_crag(userId, cragId):
        pass

    def get_all_unpublish_crags(userId):
        pass

    def get_my_unpublish_crags(userId):
        pass

    #wait on this one
    def get_all_crags__by_pins():
        pass

    def get_crags_by_state(state):
        pass

    def get_historical(cragId):
        pass