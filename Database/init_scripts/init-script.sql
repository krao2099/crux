CREATE TABLE  Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    hash_password VARCHAR(65534) NOT NULL,
    admin_flag BOOLEAN
);
INSERT INTO Users(username, email, hash_password, admin_flag) VALUES ('admin', 'admin@admin.com', 'password', TRUE);
CREATE VIEW Admins_View AS SELECT * FROM Users WHERE admin_flag = TRUE;

CREATE TABLE ClimbingArea (
    id SERIAL PRIMARY KEY,
    state VARCHAR(15),
    coordinates VARCHAR(50)[2],
    description VARCHAR(500),
    image_path VARCHAR(100),
    rating FLOAT,
    user_id INTEGER REFERENCES Users(id),
    published BOOLEAN
);

--need to add a trigger to update avgheight and maxheight on insert to routes
CREATE TABLE Wall (
    id SERIAL PRIMARY KEY,
    climbing_area_id INTEGER REFERENCES ClimbingArea(id),
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