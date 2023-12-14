class wall:
    
    def __init__(self, name, c_area, coordinates, description, image, rating, user, boulder, avgHeight=0,maxHeight=0,published=False):
        self.set_name(name)
        self.set_c_area(c_area)
        self.set_coordinates(coordinates)
        self.set_description(description)
        self.set_image(image)
        self.set_rating(rating)
        self.set_user(user)
        self.set_boulder(boulder)
        self.set_avgHeight(avgHeight)
        self.set_maxHeight(maxHeight)
        self.set_published(published)


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

    def set_user(self, user):
        self.user = user
        
    def set_boulder(self, boulder):
        self.boulder = boulder

    def set_avgHeight(self, avgHeight):
        self.avgHeight = avgHeight
    
    def set_maxHeight(self, maxHeight):
        self.maxHeight = maxHeight

    def set_published(self, published):
        self.published = published