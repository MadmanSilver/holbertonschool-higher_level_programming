-- rotten tomatoes are best tomatoes
-- do the thing
SELECT s.title, SUM(r.rate) AS rating FROM tv_shows s INNER JOIN tv_show_ratings r ON s.id=r.show_id GROUP BY s.title ORDER BY rating DESC
