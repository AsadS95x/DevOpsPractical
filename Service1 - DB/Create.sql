CREATE TABLE IF NOT EXISTS houses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    house_name
    house_location VARCHAR(50) NOT NULL,
    house_price int NOT NULL,
    date_generated DATE NOT NULL
);