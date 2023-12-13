CREATE TABLE  Users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(MAX) UNIQUE NOT NULL,
  email VARCHAR(MAX) UNIQUE NOT NULL,
  hash_password VARCHAR(MAX) NOT NULL,
  admin_flag BIT
);
INSERT INTO Users(username, email, hash_password, admin_flag) VALUES ("admin", "admin@admin.com", "password", 1);
CREATE VIEW Admins_View AS SELECT * FROM Users WHERE admin_flag = 1;
CREATE VIEW Users_View AS SELECT * FROM Users WHERE admin_flag = 0;

