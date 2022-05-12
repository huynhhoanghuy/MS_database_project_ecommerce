USE MySQLDB;

INSERT INTO PAYMENT (user_id, address_id, order_id, payment_id, payment_type, create_at, is_comlete)
VALUES
    ("1", "01", "1", "123", "MOMO", TIMESTAMP ('2022-04-02', '12:30:45'), TRUE),
    ("2", "02", "2", "456", "VISA", TIMESTAMP ('2022-04-30', '02:00:45'), FALSE),
    ("3", "03", "3", "132", "CASH", TIMESTAMP ('2022-06-02', '11:30:46'), TRUE);