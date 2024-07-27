# Write your MySQL query statement below
WITH temp AS (
    SELECT table2.user_id, COUNT(table1.title) AS movie_count
    FROM movies AS table1
    JOIN MovieRating AS table2 ON table1.movie_id = table2.movie_id
    GROUP BY table2.user_id order by count(table1.title) desc
),
result1 as (
    select table2.name as name, table1.movie_count as movie_count from temp as table1 JOIN users as table2 
    on table1.user_id = table2.user_id order by table1.movie_count desc, table2.name LIMIT 1
),
result2 as(
    SELECT table2.title AS title, AVG(table1.rating) AS avg_rating
    FROM MovieRating AS table1
    JOIN Movies AS table2 ON table1.movie_id = table2.movie_id
    WHERE table1.created_at LIKE '2020-02-%'
    GROUP BY table2.title
    ORDER BY avg_rating DESC, table2.title
    LIMIT 1
)


SELECT name AS results FROM result1
UNION ALL
SELECT title AS results FROM result2;
