SELECT * FROM User;

SELECT * FROM User
    INNER JOIN UserAddress on User.user_id=UserAddress.user_id;

UPDATE UserAddress SET city = 'Faker City' WHERE user_address_id = 2;


Common Commands:
SHOW COLUMNS FROM User;

SHOW CREATE TABLE User;

ALTER TABLE User MODIFY first_name VARCHAR(50) NOT NULL;

