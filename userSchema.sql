DROP DATABASE IF EXISTS MySQLDB;
CREATE DATABASE MySQLDB;
USE MySQLDB;

CREATE TABLE USER_INFO (
	user_id varchar(8) NOT NULL,
	user_name varchar(35) NOT NULL,
	email varchar(50) NOT NULL,
    email_verified boolean NOT NULL,
    create_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (user_id)
);

CREATE TABLE USER_ADDRESS (
    address_id varchar(8) NOT NULL,
	user_address varchar(100) NOT NULL,
	zip_code int,
	country_code int,
	is_billing boolean,
    is_shipping boolean,
	PRIMARY KEY (address_id),
	user_id varchar(8) NOT NULL,
	FOREIGN KEY (user_id)
	REFERENCES USER_INFO (user_id)
);

CREATE TABLE USER_PASSWORD (
	password_id varchar(50) NOT NULL,
    hashed_password varchar(20) NOT NULL,
    reset_in_progress boolean,
    reset_code varchar(100),
	reset_check_code varchar(100),
    reset_expires timestamp, 
    active boolean NOT NULL,
	PRIMARY KEY (password_id),
	user_id varchar(8) NOT NULL,
	FOREIGN KEY (user_id)
	REFERENCES USER_INFO (user_id)
);

CREATE TABLE SITE_VISIT (
	product_url varchar(300) NOT NULL,
	site_visit_id varchar(300) NOT NULL,
	visit_start timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	visit_last_interaction timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (site_visit_id),
	user_id varchar(8) NOT NULL,
	FOREIGN KEY (user_id)
	REFERENCES USER_INFO (user_id)
);

