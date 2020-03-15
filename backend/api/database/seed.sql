-- tbl_users
INSERT INTO `tbl_users`(
    `user_id`,
    `user_name`,
    `user_pass_hash`,
    `user_active`,
    `user_access_level`,
    `user_desc`
)
VALUES(NULL, 'admin', '123', '1', '1', 'none');

INSERT INTO `tbl_users`(
    `user_id`,
    `user_name`,
    `user_pass_hash`,
    `user_active`,
    `user_access_level`,
    `user_desc`
)
VALUES(NULL, 'jack', '123', '1', '1', 'none');


-- tbl_sessions
INSERT INTO `tbl_sessions`(
    `session_id`,
    `session_name`,
    `session_active`,
    `session_desc`
)
VALUES(NULL, 's1', '1', 'none');


-- tbl_session_data
INSERT INTO `tbl_session_data`(
    `session_data_id`,
    `session_id`,
    `session_key`,
    `session_val`
)
VALUES(NULL, '1', 'uid', '10')