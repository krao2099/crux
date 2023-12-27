import db
class Route():
    
    def __init__(self, id, date, name, grade, rating, style, height, safety, image, FA, setter, wall, numBolts, pads, coordinates, danger, description):
        self.set_id(id)
        self.set_date(date)
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

    def set_id(self, id):
        self.id = id

    def set_date(self, date):
        self.date = date
    
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

    def create_route(self):
        query = """INSERT INTO Routes (name, coordinates, grade, 
                                        rating, style, height, 
                                        safety, image_path, fa_id,
                                        setter_id, wall_id, bolts,
                                        danger) VALUES (%s, %s, %s, %s, %s
                                                                    %s, %s, %s, %s, %s,
                                                                    %s, %s, %s)"""
        record = (self.name, self.coordinates, self.grade, 
                  self.rating, self.style, self.height, 
                  self.safety, self.image, self.FA,
                  self.setter, self.wall, self.numBolts,
                  self.danger)
        try:
            db.execute(query, record)
        except Exception as e: 
            raise e

    @staticmethod
    def publish_route(route_id):
        query = """UPDATE Routes SET published = TRUE WHERE id = %s"""
        params = (route_id)
        try:
            db.execute(query, params)
        except Exception as e: 
            raise e
    
    @staticmethod
    def get_all_routes_per_crag(crag_id):
        query = """SELECT * FROM Routes WHERE crag_id = %s"""
        params = (crag_id)
        try:
            return db.retrieve(query, params)
        except Exception as e:
            raise e
    
    @staticmethod
    def get_all_routes_per_wall(wall_id):
        query = """SELECT * FROM Routes WHERE wall_id = %s"""
        params = (wall_id)
        try:
            return db.retrieve(query, params)
        except Exception as e:
            raise e
    
    @staticmethod
    def get_complete_routes(user_id):
        query = """SELECT * FROM UserRoutes WHERE completed = TRUE AND user_id = %s"""
        params = (user_id)
        try:
            return db.retrieve(query, params)
        except Exception as e:
            raise e
    
    @staticmethod
    def get_uncomplete_routes(user_id):
        query = """SELECT * FROM UserRoutes WHERE completed = FALSE AND user_id = %s"""
        params = (user_id)
        try:
            return db.retrieve(query, params)
        except Exception as e:
            raise e
    
    @staticmethod
    def get_historical(route_id):
        query = """SELECT * FROM RoutesHistorical WHERE route_id = %s ORDER BY version_number DESC"""
        params = (route_id)
        try:
            return db.retrieve(query, params)
        except Exception as e:
            raise e