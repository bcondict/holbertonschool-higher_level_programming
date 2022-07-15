-- lists all show contained in a datebase
--      if show doesn't have a genre display NULL
SELECT tv_shows.title, tv_shows.genre_id FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
ORDER BY tv_shows.title ASC, tv_shows_genres.genre_id ASC;