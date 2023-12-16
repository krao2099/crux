CREATE TABLE  Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    hash_password VARCHAR(65534) NOT NULL,
    admin_flag BOOLEAN
);

--create an admin user in the db for testing purposes
INSERT INTO Users(username, email, hash_password, admin_flag) VALUES ('admin', 'admin@admin.com', 'password', TRUE);
CREATE VIEW Admins AS SELECT * FROM Users WHERE admin_flag = TRUE;

CREATE TABLE Crags (
    id SERIAL PRIMARY KEY,
    state VARCHAR(15),
    coordinates VARCHAR(50)[2],
    description VARCHAR(500),
    image_path VARCHAR(100),
    rating FLOAT,
    user_id INTEGER REFERENCES Users(id),
    published BOOLEAN
);

--allow for easy returning of published vs unpublished areas
CREATE VIEW PublishedCrags AS SELECT * FROM Crags WHERE published = TRUE;
CREATE VIEW UnpublishedCrags AS SELECT * FROM Crags WHERE published = FALSE;

--need to add a trigger to update avgheight and maxheight on insert to routes
CREATE TABLE Walls (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    climbing_area_id INTEGER REFERENCES Crags(id),
    coordinates VARCHAR(50)[2],
    description VARCHAR(500),
    image_path VARCHAR(100),
    rating FLOAT,
    user_id INTEGER REFERENCES Users(id),
    avg_height FLOAT,
    max_height FLOAT,
    published BOOLEAN,
    boulder BOOLEAN
);

--allow for easy returning of published vs unpublished walls
CREATE VIEW PublishedWalls AS SELECT * FROM Walls WHERE published = TRUE AND boulder = FALSE;
CREATE VIEW UnpublishedWalls AS SELECT * FROM Walls WHERE published = FALSE AND boulder = FALSE;
CREATE VIEW PublishedBoulders AS SELECT * FROM Walls WHERE published = TRUE AND boulder = TRUE;
CREATE VIEW UnpublishedBoulders AS SELECT * FROM Walls WHERE published = FALSE AND boulder = TRUE;

CREATE TABLE Routes (
    id SERIAL PRIMARY KEY,
    grade VARCHAR(4),
    rating FLOAT,
    style VARCHAR(50),
    height FLOAT,
    safety VARCHAR(50),
    image_path VARCHAR(100),
    fa_id INTEGER REFERENCES Users(id),
    setter_id INTEGER REFERENCES Users(id),
    wall_id INTEGER REFERENCES Walls(id)
);

--historical tables will all have the same fields as the others, and a version number
CREATE TABLE CragsHistorical (
    id SERIAL PRIMARY KEY,
    climbing_area_id INTEGER REFERENCES Crags(id),
    version_number INTEGER,
    state VARCHAR(15),
    coordinates VARCHAR(50)[2],
    description VARCHAR(500),
    image_path VARCHAR(100),
    rating FLOAT,
    user_id INTEGER REFERENCES Users(id),
    published BOOLEAN
);

CREATE TABLE WallsHistorical (
    id SERIAL PRIMARY KEY,
    wall_id INTEGER REFERENCES Walls(id),
    version_number INTEGER,
    name VARCHAR(100),
    climbing_area_id INTEGER REFERENCES Crags(id),
    coordinates VARCHAR(50)[2],
    description VARCHAR(500),
    image_path VARCHAR(100),
    rating FLOAT,
    user_id INTEGER REFERENCES Users(id),
    avg_height FLOAT,
    max_height FLOAT,
    published BOOLEAN,
    boulder BOOLEAN
);

CREATE TABLE RoutesHistorical(
    id SERIAL PRIMARY KEY,
    route_id INTEGER REFERENCES Routes(id),
    version_number INTEGER,
    grade VARCHAR(4),
    rating FLOAT,
    style VARCHAR(50),
    height FLOAT,
    safety VARCHAR(50),
    image_path VARCHAR(100),
    fa_id INTEGER REFERENCES Users(id),
    setter_id INTEGER REFERENCES Users(id),
    wall_id INTEGER REFERENCES Walls(id)
);

--users can make comments on routes, and save routes as completed or to-do
CREATE TABLE RouteComments(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(id),
    route_id INTEGER REFERENCES Routes(id),
    comment VARCHAR(500),
    date DATE
);

CREATE TABLE UserRoutes(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(id),
    route_id INTEGER REFERENCES Routes(id),
    completed BOOLEAN
);

--need to update the stored max height and average height for a wall when any of its routes are modified
CREATE FUNCTION update_heights() RETURNS TRIGGER AS $$
    DECLARE
        max FLOAT;
        avg FLOAT;
    BEGIN
        SELECT MAX(height) INTO max FROM Routes WHERE wall_id = OLD.wall_id;
        SELECT AVG(height) INTO avg FROM Routes WHERE wall_id = OLD.wall_id;

        UPDATE Walls SET avg_height = avg, max_height = max WHERE id = OLD.wall_id;
    END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER height_inserts
    AFTER INSERT OR UPDATE OR DELETE ON Routes
    FOR EACH ROW EXECUTE FUNCTION update_heights();

--archive functions will run when a climbing area/wall/route are updated to save the old version
CREATE FUNCTION archive_climbing_area() RETURNS TRIGGER AS $$
    DECLARE
        version INTEGER;
    BEGIN
        SELECT MAX(version_number) + 1 INTO version FROM CragsHistorical WHERE climbing_area_id = OLD.id;
        INSERT INTO CragsHistorical (version_number,
                                                climbing_area_id,
                                                state,
                                                coordinates,
                                                description,
                                                image_path,
                                                rating,
                                                user_id,
                                                published
                                            ) VALUES (
                                                version,
                                                OLD.id,
                                                OLD.coordinates,
                                                OLD.description,
                                                OLD.image_path,
                                                OLD.rating,
                                                OLD.user_id,
                                                OLD.published    
                                            );
    END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER update_climbing_areas
    AFTER UPDATE ON Crags
    FOR EACH ROW EXECUTE FUNCTION archive_climbing_area();

CREATE FUNCTION archive_wall() RETURNS TRIGGER AS $$
    DECLARE
        version INTEGER;
    BEGIN
        SELECT MAX(version_number) + 1 INTO version FROM WallsHistorical WHERE wall_id = OLD.id;
        INSERT INTO WallsHistorical (version_number,
                                        wall_id,
                                        name,
                                        climbing_area_id,
                                        coordinates,
                                        description,
                                        image_path ,
                                        rating,
                                        user_id,
                                        avg_height,
                                        max_height,
                                        published,
                                        boulder
                                    ) VALUES (
                                        version,
                                        OLD.id,
                                        OLD.name,
                                        OLD.climbing_area_id,
                                        OLD.coordinates,
                                        OLD.description,
                                        OLD.image_path ,
                                        OLD.rating,
                                        OLD.user_id,
                                        OLD.avg_height,
                                        OLD.max_height,
                                        OLD.published,
                                        OLD.boulder  
                                    );
    END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER update_climbing_areas
    AFTER UPDATE ON Walls
    FOR EACH ROW EXECUTE FUNCTION archive_wall();

CREATE FUNCTION archive_route() RETURNS TRIGGER AS $$
    DECLARE
        version INTEGER;
    BEGIN
        SELECT MAX(version_number) + 1 INTO version FROM RoutesHistorical WHERE route_id = OLD.id;
        INSERT INTO RoutesHistorical (route_id,
                                        version_number,
                                        grade,
                                        rating,
                                        style,
                                        height,
                                        safety,
                                        image_path,
                                        fa_id,
                                        setter_id,
                                        wall_id
                                    ) VALUES (
                                        OLD.id,
                                        version,
                                        OLD.grade,
                                        OLD.rating,
                                        OLD.style,
                                        OLD.height,
                                        OLD.safety,
                                        OLD.image_path,
                                        OLD.fa_id,
                                        OLD.setter_id,
                                        OLD.wall_id  
                                    );
    END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER update_routes
    AFTER UPDATE ON Routes
    FOR EACH ROW EXECUTE FUNCTION archive_route();


