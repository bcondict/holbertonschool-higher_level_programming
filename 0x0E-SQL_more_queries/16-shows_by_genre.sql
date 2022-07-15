-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_genres.name FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
LEFT JOIN tv_genres ON tv_shows_genres.genre_id = tv_genres.id 
ORDER BY tv_shows.title, tv_genres.name;