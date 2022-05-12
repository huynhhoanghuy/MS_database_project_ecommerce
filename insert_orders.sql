INSERT INTO
  ORDERS (order_id, cost, user_id)
VALUES
  (1, 50000, 1);

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
  ORDERS (order_id, cost, user_id)
VALUES
  (2, 12000, 2);

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