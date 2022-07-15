-- create a database and a table (inside database)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    PRIMARY KEY(id),
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
    name VARCHAR(256) NOT NULL,
);