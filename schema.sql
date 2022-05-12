CREATE TABLE TEAM_PRODUCT (
	product_id int NOT NULL,
	product_name varchar(100) NOT NULL,
	taxon_id int NOT NULL,
	num_view int,
	PRIMARY KEY (product_id)
);

CREATE TABLE TEAM_TAXON (
	taxon_id int NOT NULL,
	parent_id int,
	taxon_name varchar(100) NOT NULL,

	PRIMARY KEY (taxon_id)
);
