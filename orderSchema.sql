CREATE TABLE ORDERS (
  order_id varchar(8) NOT NULL,
  create_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  cost float(2),
  user_id int NOT NULL,
  PRIMARY KEY (order_id),
  FOREIGN KEY (user_id) REFERENCES USER_INFO(user_id)
);

CREATE TABLE ORDER_PRODUCT (
  order_id varchar(8) NOT NULL,
  product_id varchar(8) NOT NULL,
  cost float(2),
  quantity int NOT NULL,
  PRIMARY KEY (order_id, product_id),
  FOREIGN KEY (order_id) REFERENCES ORDERS(order_id)
);

CREATE TABLE SHIPPING (
  shipping_id varchar(8) NOT NULL,
  shipping_status char(4),
  order_id varchar(8) NOT NULL,
  address_id int NOT NULL,
  PRIMARY KEY (shipping_id),
  FOREIGN KEY (order_id) REFERENCES ORDERS(order_id),
  FOREIGN KEY (address_id) REFERENCES USER_ADDRESS(address_id)
);