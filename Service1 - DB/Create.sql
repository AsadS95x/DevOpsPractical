CREATE DATABASE IF NOT EXISTS housesdb;

CREATE TABLE IF NOT EXISTS houses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    house_location VARCHAR(50) NOT NULL,
    house_size int NOT NULL,
    house_price int NOT NULL,
    date_generated DATE NOT NULL
);

