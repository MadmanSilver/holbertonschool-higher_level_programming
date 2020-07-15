-- rotten tomatoes are best tomatoes
-- do the thing
SELECT g.name, SUM(r.rate) AS rating FROM tv_shows s INNER JOIN tv_show_ratings r ON s.id=r.show_id INNER JOIN tv_show_genres sg ON s.id=sg.show_id INNER JOIN tv_genres g ON sg.genre_id=g.id GROUP BY g.name ORDER BY rating DESC
