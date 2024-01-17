<<<<<<< HEAD
-- script that uses the hbtn_0d_tvshows to list all genres not linked to Dexter.
SELECT DISTINCT tv_genres.name FROM tv_genres JOIN tv_show_genres JOIN tv_shows
ON tv_genres.id = tv_show_genres.genre_id
and tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title <> 'Dexter'
ORDER BY tv_genres.name;
=======
-- Lists all genres of the database hbtn_0d_tvshows
-- not linked to the show Dexter.
-- Records are sorted by ascending genre name.
SELECT DISTINCT `name`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`

       INNER JOIN `tv_shows` AS t
       ON s.`show_id` = t.`id`
       WHERE g.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS g
	             INNER JOIN `tv_show_genres` AS s
		     ON g.`id` = s.`genre_id`

		     INNER JOIN `tv_shows` AS t
		     ON s.`show_id` = t.`id`
		     WHERE t.`title` = "Dexter")
 ORDER BY g.`name`;
>>>>>>> 9b8b5f338237880234c10eda7cb93d0545c798be
