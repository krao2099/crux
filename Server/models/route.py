class route:
    
    def __init__(self, name, grade, rating, style, height, safety, image, FA, setter, wall):
        self.set_name(name)
        self.set_grade(grade)
        self.set_rating(rating)
        self.set_style(style)
        self.set_height(height)
        self.set_safety(safety)
        self.set_image(image)
        self.set_FA(FA)
        self.set_setter(setter)
        self.set_wall(wall)

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