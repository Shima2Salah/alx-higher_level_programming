-- script that uses the hbtn_0d_tvshows to list all genres not linked to Dexter.
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating FROM tv_shows JOIN tv_show_genres JOIN tv_show_ratings
ON tv_shows.id = tv_show_genres.show_id
AND tv_show_genres.show_id = tv_show_ratings.show_id
ORDER BY rating DESC;
