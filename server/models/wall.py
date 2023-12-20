import db
class Wall():
    
    def __init__(self, id, date, name, crag_id, coordinates, description, image, rating, user, boulder, directions, avgHeight=0,maxHeight=0):
        self.set_id(id)
        self.set_date(date)
        self.set_name(name)
        self.set_crag_id(crag_id) #FK to crag
        self.set_coordinates(coordinates)
        self.set_description(description)
        self.set_image(image)
        self.set_rating(rating)
        self.set_user(user)
        self.set_boulder(boulder)
        self.set_directions(directions)
        self.set_avgHeight(avgHeight)
        self.set_maxHeight(maxHeight)

    def set_id(self, id):
        self.id = id

    def set_date(self, date):
        self.date = date

    def set_name(self, name):
        self.name = name

    def set_crag_id(self, crag_id):
        self.crag_id = crag_id
    
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

    def set_directions(self, directions):
        self.directions = directions

    def set_avgHeight(self, avgHeight):
        self.avgHeight = avgHeight
    
    def set_maxHeight(self, maxHeight):
        self.maxHeight = maxHeight

    def create_wall(self):
        query = """INSERT INTO Walls (name, crag_id, coordinates, description, 
                                        image_path, rating, user_id, 
                                        boulder, directions) VALUES (%s, %s, %s, %s, 
                                                                                %s, %s, %s, %s, %s)"""
        record = (self.name, self.crag_id, self.coordinates, 
                  self.description, self.image_path, self.rating, 
                  self.user_id, self.boulder, self.directions)
        try:
            db.execute(query, record)
        except Exception as e: 
            raise e

    def publish_wall(wall_id):
        query = """UPDATE Walls SET published = TRUE WHERE id = %s"""
        params = (wall_id)
        try:
            db.execute(query, params)
        except Exception as e: 
            raise e

    def get_walls_per_crag(crag_id):
        query = """SELECT COUNT(*) FROM Walls WHERE crag_id = %s"""
        params = (crag_id)
        try:
            return db.execute(query, params)
        except Exception as e:
            raise e

    def get_all_walls():
        query = """SELECT * FROM Walls"""
        try:
            return db.execute(query)
        except Exception as e:
            raise e

    def get_historical(wall_id):
        query = """SELECT * FROM WallsHistorical WHERE wall_id = %s ORDER BY version_number DESC"""
        params = (wall_id)
        try:
            return db.execute(query, params)
        except Exception as e:
            raise e