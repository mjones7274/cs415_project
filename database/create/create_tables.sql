CREATE TABLE User (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(40) NOT NULL,
    pass_word VARCHAR(40) NOT NULL,
    created_date DATETIME,
    is_active BOOLEAN,
    last_login DATETIME,
    PRIMARY KEY (user_id),
    UNIQUE (email)
);

CREATE TABLE AddressType (
    address_type_id INT NOT NULL AUTO_INCREMENT,
    address_type VARCHAR(10) NOT NULL,
    PRIMARY KEY (address_type_id)
);

CREATE TABLE UserAddress (
    user_address_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    address_type_id INT NOT NULL,
    address_1 VARCHAR(30),
    address_2 VARCHAR(30),
    city VARCHAR(25),
    st VARCHAR(2),
    zip VARCHAR(10),
    country VARCHAR(30),
    PRIMARY KEY (user_address_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (address_type_id) REFERENCES AddressType(address_type_id)
);

CREATE TABLE UserInfo (
    user_info_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    profile_bio VARCHAR(500),
    profile_picture VARCHAR(100),
    modified_date DATETIME,
    created_date DATETIME,
    PRIMARY KEY (user_info_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE PhoneType (
    phone_type_id INT NOT NULL AUTO_INCREMENT,
    phone_type VARCHAR(10) NOT NULL,
    PRIMARY KEY (phone_type_id)
);

CREATE TABLE UserPhone (
    user_phone_id INT NOT NULL AUTO_INCREMENT,
    phone_type_id INT NOT NULL,
    user_id INT NOT NULL,
    phone_number VARCHAR(10),
    created_date DATETIME,
    is_active BOOLEAN,
    PRIMARY KEY (user_phone_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (phone_type_id) REFERENCES PhoneType(phone_type_id)
);

CREATE TABLE PageData (
    page_data_id INT NOT NULL AUTO_INCREMENT,
    page_name VARCHAR(25) NOT NULL,
    page_title VARCHAR(25) NOT NULL,
    page_description VARCHAR(150) NOT NULL,
    page_picture VARCHAR(100),
    PRIMARY KEY (page_data_id)
);





