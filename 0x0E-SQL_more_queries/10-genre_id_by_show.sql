-- List all shows in hbtn_0d_tvshows with at least one genre linked
SELECT tv_shows.title, tv_show_genre.genre_id FROM tv_shows LEFT JOIN tv_show_genre ON tv_shows.id = tv_show_genre.show_id WHERE tv_show_genre.genre_id IS NOT NULL ORDER BY tv_shows.title, tv_show_genre.genre_id;
