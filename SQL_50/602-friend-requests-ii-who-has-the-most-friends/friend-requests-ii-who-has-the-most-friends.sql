# Write your MySQL query statement below
with base as(select requester_id id from RequestAccepted
union all
select accepter_id id from RequestAccepted)

SELECT
    id,
    count(*) as num
FROM
    base
GROUP BY 
    id
ORDER BY
    num desc
limit 1;

