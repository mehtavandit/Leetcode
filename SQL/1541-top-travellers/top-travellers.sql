# Write your MySQL query statement below
SELECT
    u.name as name, COALESCE(sum(r.distance),0) as travelled_distance
FROM Users as u
LEFT JOIN Rides as r
ON u.id = r.user_id
group by u.id
order by travelled_distance desc, name;