DROP
    DATABASE IF EXISTS db_test_1;

CREATE DATABASE IF NOT EXISTS db_test_1 CHARSET = utf8 COLLATE utf8_bin; 

CREATE TABLE `db_test_1`.`tbl_users`(
    `user_id` INT NOT NULL AUTO_INCREMENT,
    `user_name` VARCHAR(200) NOT NULL,
    `user_pass_hash` INT(200) NOT NULL,
    `user_active` INT NOT NULL,
    `user_access_level` INT NOT NULL,
    `user_desc` VARCHAR(500) NOT NULL,
    PRIMARY KEY(`user_id`)
) ENGINE = InnoDB CHARSET = utf8 COLLATE utf8_bin;

CREATE TABLE `db_test_1`.`tbl_sessions`(
    `session_id` INT NOT NULL AUTO_INCREMENT,
    `session_name` VARCHAR(200) NOT NULL,
    `session_active` INT NOT NULL,
    `session_desc` VARCHAR(500) NULL,
    PRIMARY KEY(`session_id`),
    UNIQUE (`session_name`)
) ENGINE = InnoDB CHARSET = utf8 COLLATE utf8_bin; 

CREATE TABLE `db_test_1`.`tbl_session_data`(
    `session_data_id` INT NOT NULL AUTO_INCREMENT,
    `session_id` INT NOT NULL,
    `session_key` VARCHAR(500) NOT NULL,
    `session_val` VARCHAR(500) NOT NULL,
    PRIMARY KEY(`session_data_id`),
    FOREIGN KEY (session_id) REFERENCES tbl_sessions(session_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB CHARSET = utf8 COLLATE utf8_bin;

-- Add other tables here