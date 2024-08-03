# Write your MySQL query statement below
select sell_date, count(distinct product) as num_sold, 
GROUP_CONCAT(Distinct product order by product separator ',') AS products 
from activities group by sell_date;