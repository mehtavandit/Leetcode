# Write your MySQL query statement below
select query_name, 
round((sum(q.rating / q.position))/count(q.query_name),2) as quality,
round(avg(if(rating < 3, 1, 0))*100 , 2) as poor_query_percentage
from Queries q where q.query_name is not Null group by q.query_name;