-- lists all Comedy shows in a datebase
SELECT tv_shows.title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title, tv_genres.name;