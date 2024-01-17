-- script that lists all cities contained in the database hbtn_0d_usa.
SELECT tv_genres.name AS genre, COUNT(show_id.tv_show_genres) AS number_of_shows FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id ORDER BY number_of_shows DESC;

