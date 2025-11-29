-- jbnb
SELECT tg.genre_id AS genre, COUNT(tg.show_id) AS number_of_shows
FROM tv_show_genres tg
JOIN tv_shows ts
ON tg.show_id = ts.id
GROUP BY tg.genre_id
ORDER BY number_of_shows DESC;

