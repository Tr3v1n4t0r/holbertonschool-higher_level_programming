-- List all shows in hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genre.genre_id FROM tv_shows LEFT JOIN tv_show_genre ON tv_shows.id = tv_show_genre.show_id ORDER BY tv_shows.title, tv_show_genre.genre_id;
