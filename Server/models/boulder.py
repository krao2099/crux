class wall:
    
    def __init__(self, name, c_area, coordinates, description, image, rating, avgHeight=0,maxHeight=0, published=False):
        self.set_name(name)
        self.set_c_area(c_area)
        self.set_coordinates(coordinates)
        self.set_description(description)
        self.set_image(image)
        self.set_rating(rating)

    def set_name(self, name):
        self.name = name

    def set_c_area(self, c_area):
        self.c_area = c_area
    
    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def set_description(self, description):
        self.description = description

    def set_image(self, image):
        self.image = image


    def set_rating(self, rating):
        self.rating = rating