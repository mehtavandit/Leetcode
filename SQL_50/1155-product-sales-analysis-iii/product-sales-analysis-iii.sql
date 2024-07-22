# Write your MySQL query statement below
WITH temp as (
    SELECT product_id, min(year) as first_year
    from Sales group by product_id
)

select s.product_id, s.year as first_year, s.quantity, s.price
from sales s JOIN temp on s.product_id = temp.product_id AND s.year = temp.first_year; 