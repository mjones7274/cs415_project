CREATE TABLE User (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(25),
    last_name VARCHAR(30),
    email VARCHAR(40),
    pass_word VARCHAR(40),
    created_date DATETIME,
    is_active BOOLEAN,
    PRIMARY KEY (user_id)
);

CREATE TABLE UserAddress (
    user_address_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    address_1 VARCHAR(30),
    address_2 VARCHAR(30),
    city VARCHAR(25),
    st VARCHAR(2),
    zip VARCHAR(10),
    country VARCHAR(30),
    PRIMARY KEY (user_address_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);





