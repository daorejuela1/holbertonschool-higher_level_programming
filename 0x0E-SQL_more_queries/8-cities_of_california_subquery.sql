-- join info from two tables
-- not using the world join
SELECT id, name FROM cities WHERE (SELECT id FROM states WHERE name = "California") ORDER BY id ASC;
