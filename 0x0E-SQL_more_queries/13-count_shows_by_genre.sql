-- lists all shows contained in a datebase without a genre linked
SELECT tv_genres.name, COUNT(tv_shows_genres.genre_id) AS MY_COUNT FROM tv_shows_genres
RIGHT JOIN tv_genres ON tv_genres.id = tv_shows_genres.genre_id
GROUP BY tv_genres.name
ORDER BY MY_COUNT DESC;