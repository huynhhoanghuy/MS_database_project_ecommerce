USE MySQLDB;

INSERT INTO USER_INFO (user_id, user_name, email, email_verified, create_at)
VALUES
    ("1", "Harry", "harry.gryffindor@gmail.com", TRUE, TIMESTAMP ('2022-03-23', '12:30:45')),
    ("2", "Ron", "ron@gmail.com", TRUE, TIMESTAMP ('2022-04-22', '23:30:45')),
    ("3", "Hermione", "hermi@gmail.com", FALSE, TIMESTAMP ('2022-05-01', '11:30:45'));

INSERT INTO USER_ADDRESS (user_id, address_id, user_address, zip_code, country_code, is_billing, is_shipping)
VALUES
    ("1", "01", "220 Nguyen Van Cu, p4, Q.5, TPHCM", 84, 74000, TRUE, TRUE),
    ("2", "02", "221 , Phan Chau Trinh, Q.Hai Chau, Da Nang", 84, 50000, TRUE, FALSE),
    ("3", "03", "222 Hoang Dieu, Q.Ba Dinh, Ha Noi", 18000, 84, FALSE, FALSE);

INSERT INTO USER_PASSWORD (user_id, password_id, hashed_password, reset_in_progress, reset_code, reset_check_code, reset_expires, active)
VALUES
    ("1", "1234", "ab4343x", TRUE, "345", "345", TIMESTAMP ('2022-03-23', '13:00:15'), TRUE),
    ("2", "1324", "ng89xhj", TRUE, "345", "147", TIMESTAMP ('2022-04-23', '02:00:45'), FALSE),
    ("3", "1423", "9dsadft", TRUE, "345", " ", TIMESTAMP ('2022-05-02', '22:30:11'), FALSE);

INSERT INTO SITE_VISIT (user_id, product_url, site_visit_id, visit_start, visit_last_interaction)
VALUES
    ("1", "sBydsads.html", "2345", TIMESTAMP ('2022-03-23', '12:30:45'), TIMESTAMP ('2022-03-23', '12:30:45')),
    ("2", "sBydsads.html", "3245", TIMESTAMP ('2022-04-30', '02:00:45'), TIMESTAMP ('2022-04-30', '02:05:50')),
    ("3", "sBydsads.html", "3435", TIMESTAMP ('2022-06-02', '12:30:45'), TIMESTAMP ('2022-06-02', '12:30:46'));

INSERT INTO PAYMENT (user_id, address_id, order_id, payment_id, payment_type, create_at, is_comlete)
VALUES
    ("1", "01", "080231", "123", "MOMO", TIMESTAMP ('2022-04-02', '12:30:45'), TRUE),
    ("2", "02", "3123F4", "456", "VISA", TIMESTAMP ('2022-04-30', '02:00:45'), FALSE),
    ("3", "03", "DS3213", "132", "CASH", TIMESTAMP ('2022-06-02', '11:30:46'), TRUE);

INSERT INTO E_WALLET (user_id, name_wallet, is_verified)
VALUES
    ("1", "MOMO", TRUE),
    ("2", "ZaloPay", TRUE),
    ("3", "ViettelPay", FALSE);