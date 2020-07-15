-- show stuff
-- do it
SELECT title FROM tv_shows WHERE title NOT IN (SELECT s.title FROM tv_shows s INNER JOIN tv_show_genres sg ON s.id=sg.show_id INNER JOIN tv_genres g ON sg.genre_id=g.id WHERE g.name = 'Comedy') ORDER BY title ASC
