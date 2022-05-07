USE TEAM;

INSERT INTO TEAM_TAXON (taxon_id, parent_id, taxon_name)
VALUES
	(0, 0, "MEN" ),
	(1, 0, "WOMEN");

INSERT INTO TEAM_TAXON (taxon_id, parent_id, taxon_name)
VALUES
	(2, 0, "SHIRT" ),
	(3, 0, "PANTS");
;

INSERT INTO TEAM_TAXON (taxon_id, parent_id, taxon_name)
VALUES
	(4, 1, "SKIRT" ),
	(5, 1, "SHOES");

