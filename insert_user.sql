USE USERS;

INSERT INTO USER_INFO (user_id, user_name, email, email_verified, create_at)
VALUES
    (1, "Harry", "harry.gryffindor@gmail.com", TRUE, "2022-03-23 12:00"),
    (2, "Ron", "ron@gmail.com", TRUE, "2022-04-30 22:00"),
    (3, "Hermione", hermi@gmail.com, FALSE, "2022-05-1 23:23");

INSERT INTO USER_ADDRESS (user_id, address_id, user_address, zip_code, is_billing, is_shipping)
VALUES
    (1, 01, "220 Nguyen Van Cu, p4, Q.5, TPHCM", 74000, TRUE, TRUE),
    (2, 02, "221 , Phan Chau Trinh, Q.Hai Chau, Da Nang", 50000, TRUE, FALSE),
    (3, 03, "222 Hoang Dieu, Q.Ba Dinh, Ha Noi", 18000, FALSE, FALSE);

INSERT INTO USER_PASSWORD (user_id, password_id, hashed_password, reset_in_progress, reset_code, reset_check_code, reset_expires, active)
VALUES
    (1, ),
    (2, ),
    (3, );

INSERT INTO SITE_VISIT (user_id, product_url, site_visit_id, visit_start, visit_last_interaction)
VALUES
    (1, ),
    (2, ),
    (3, );