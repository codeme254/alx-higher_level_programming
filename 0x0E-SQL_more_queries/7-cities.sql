-- creates the database hbtn_0d_usa and the table cities in db hbtn_0d_usa
-- id INT unique auto generated, can't be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY
--          that references to id of the states table
-- name VARCHAR 256 and can't be null
-- if either the db or the table exists, the script should not fail

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities`(
    `id` INT UNIQUE NOT NULL AUTO_INCREMENT,
    `state_id` INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`state_id`) REFERENCES `hbtn_0d_usa`.`states`(`id`)
);
