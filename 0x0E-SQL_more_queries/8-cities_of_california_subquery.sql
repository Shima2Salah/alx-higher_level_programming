-- script that lists all the cities of California in hbtn_0d_usa.
SELECT hbtn_0d_usa FROM states.cities 
WHERE  name = California ORDER BY cities.id;
