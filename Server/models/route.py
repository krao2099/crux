from base import base

class route(base):
    
    def __init__(self, id, date, name, grade, rating, style, height, safety, image, FA, setter, wall, numBolts, pads, coordinates, danger, description, published=False):
        super().__init__(id,date)
        self.set_name(name)
        self.set_grade(grade)
        self.set_rating(rating)
        self.set_style(style)
        self.set_height(height)
        self.set_safety(safety)
        self.set_image(image)
        self.set_FA(FA)
        self.set_setter(setter)
        self.set_wall(wall) #FK to walls
        self.set_numBolts(numBolts)
        self.set_pads(pads)
        self.set_coordinates(coordinates)
        self.set_danger(danger)
        self.set_description(description)
        self.set_published(published)

    def set_name(self, name):
        self.name = name

    def set_grade(self, grade):
        self.grade = grade

    def set_rating(self, rating):
        self.rating = rating

    def set_style(self, style):
        self.style = style

    def set_height(self, height):
        self.height = height

    def set_safety(self, safety):
        self.safety = safety

    def set_image(self, image):
        self.image = image

    def set_FA(self, FA):
        self.FA = FA

    def set_setter(self, setter):
        self.setter = setter

    def set_wall(self, wall):
        self.wall = wall

    def set_numBolts(self, numBolts):
        self.numBolts = numBolts

    def set_pads(self, pads):
        self.pads = pads

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def set_danger(self, danger):
        self.danger = danger

    def set_description(self, description):
        self.description = description

    def set_published(self, published):
        self.published = published

    def create_route(self):
        pass

    def edit_route(self, name, grade, rating, style, height, safety, image, FA, setter, wall, numBolts, pads, coordinates, danger, description):
        pass

    def publish_route(routeId):
        pass

    def get_all_routes_per_crag(cragId):
        pass

    def get_all_routes_per_wall(wallId):
        pass

    def get_complete_routes(userid):
        pass

    def get_uncomplete_routes(userid):
        pass

    def get_historical(routeId):
        pass