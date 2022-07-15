-- lists all Comedy shows in a datebase
SELECT tv_shows.title FROM tv_shows
INNER JOIN tv_shows_genres ON tv_shows_genres.show_id - tv_shows.id
INNER JOIN tv_genres ON tv_genres.id = tv_shows_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;