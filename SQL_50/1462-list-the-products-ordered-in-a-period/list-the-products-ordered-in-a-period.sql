# Write your MySQL query statement below
WITH temp as(
    select * from orders where YEAR(order_date) = 2020 and MONTH(order_date) = 2
)
-- select * from temp;

select table1.product_name, SUM(table2.unit) as unit from products as table1
JOIN temp as table2 ON table1.product_id = table2.product_id
group by table1.product_name Having(unit > 99);