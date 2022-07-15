-- lists all show contained in a datebase that have at least one genre linked
SELECT tv_shows.title, tv_shows.genre_id FROM tv_shows
INNER JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
ORDER BY tv_shows.title ASC, tv_shows_genres.genre_id ASC;