-- creates the table force_name on your MySQL server.
-- id: int, name varchar(256) and can't be null
-- he database name will be passed as an argument of the mysql command
-- cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2

CREATE TABLE IF NOT EXISTS `force_name`(
    `id` INT,
    `name` VARCHAR(256) NOT NULL
);

