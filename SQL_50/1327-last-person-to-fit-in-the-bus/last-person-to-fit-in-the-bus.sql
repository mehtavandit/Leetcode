# Write your MySQL query statement below
WITH temp as (
    select *, sum(weight) over(order by turn) as cum from queue
)

select person_name from temp where cum<=1000 order by turn desc limit 1;