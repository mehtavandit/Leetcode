# Write your MySQL query statement below
WITH TEMP AS(
    SELECT buyer_id, count(order_id) as order_in_2019
    FROM orders where YEAR(order_date) = 2019
    group by buyer_id
)

SELECT u.user_id as buyer_id,u.join_date,COALESCE(t.order_in_2019,0) as orders_in_2019
FROM Users u
LEFT JOIN temp t
ON u.user_id = t.buyer_id;