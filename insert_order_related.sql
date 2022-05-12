USE MySQLDB;

INSERT INTO
  ORDER_PRODUCT (order_id, product_id, cost, quantity)
VALUES
  (1, 1, 10000, 1);

INSERT INTO
  SHIPPING (
    shipping_id,
    order_id,
    address_id,
    shipping_status
  )
VALUES
  (1, 1, 1, "DELI");

INSERT INTO
  ORDER_PRODUCT (order_id, product_id, cost, quantity)
VALUES
  (2, 1, 10000, 1),
  (2, 2, 2000, 2);

INSERT INTO
  SHIPPING (
    shipping_id,
    order_id,
    address_id,
    shipping_status
  )
VALUES
  (2, 2, 2, "RECI");