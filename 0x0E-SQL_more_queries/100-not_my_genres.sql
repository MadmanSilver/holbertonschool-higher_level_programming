-- show stuff
-- do it
SELECT name FROM tv_genres WHERE name NOT IN (SELECT g.name FROM tv_shows s INNER JOIN tv_show_genres sg ON s.id=sg.show_id INNER JOIN tv_genres g ON sg.genre_id=g.id WHERE s.title = 'Dexter') ORDER BY name ASC
