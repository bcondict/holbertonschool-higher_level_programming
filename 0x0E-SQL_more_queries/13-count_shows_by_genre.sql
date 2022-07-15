-- lists all shows contained in a datebase without a genre linked
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS MY_COUNT
RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY MY_COUNT DESC;