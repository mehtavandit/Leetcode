# Write your MySQL query statement below
select customer_id from customer group by customer_id
HAVING count(distinct product_key) = (Select count(product_key) from product)