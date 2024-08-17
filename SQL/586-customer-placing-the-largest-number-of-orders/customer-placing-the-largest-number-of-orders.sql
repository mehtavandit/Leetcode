# Write your MySQL query statement below
SELECT
    customer_number
FROM Orders
GROUP By customer_number order by count(*) DESC LIMIT 1;