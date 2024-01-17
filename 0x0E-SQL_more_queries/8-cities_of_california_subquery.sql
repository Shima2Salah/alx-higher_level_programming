-- script that lists all the cities of California in hbtn_0d_usa.
SELECT id, name FROM states.cities 
WHERE  name = California ORDER BY cities.id;
