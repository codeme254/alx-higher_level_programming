-- creates the table unique_id on your MySQL server.
-- id INT with default value of 1 and must be unique
-- name varchar(256)
-- database name will be passed as an argument of the mysql command
-- if the table already exists, your script should not fail

CREATE TABLE IF NOT EXISTS `unique_id`(
    `id` INT UNIQUE DEFAULT 1,
    `name` VARCHAR(256)
);

