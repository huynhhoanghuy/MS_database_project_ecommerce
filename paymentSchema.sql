USE MySQLDB;

CREATE TABLE PAYMENT (
    payment_id varchar(8) NOT NULL,
    payment_type varchar(4) NOT NULL,
    create_at timestamp NOT NULL,
    is_comlete boolean,
    
    PRIMARY KEY (payment_id),
    order_id varchar(8) NOT NULL, 


    address_id varchar(8) NOT NULL,
    FOREIGN KEY (address_id)
	REFERENCES USER_ADDRESS (address_id),

    user_id varchar(8) NOT NULL,
	FOREIGN KEY (user_id)
	REFERENCES USER_INFO (user_id)
);

CREATE TABLE E_WALLET (
    name_wallet varchar(15) NOT NULL,
    is_verified boolean NOT NULL,
    PRIMARY KEY (name_wallet),

    user_id varchar(8) NOT NULL,
	FOREIGN KEY (user_id)
	REFERENCES USER_INFO (user_id)
);

