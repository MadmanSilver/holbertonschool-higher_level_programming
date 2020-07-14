-- genre stuff
-- do it
SELECT g.name AS genre, COUNT(s.genre_id) AS number_of_shows FROM tv_genres g INNER JOIN tv_show_genres s ON g.id=s.genre_id GROUP BY s.genre_id ORDER BY number_of_shows DESC
