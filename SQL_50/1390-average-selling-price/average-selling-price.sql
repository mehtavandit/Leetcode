# Write your MySQL query statement below
select p.product_id, IFNULL(ROUND(sum(u.units*p.price)/sum(u.units),2),0) as average_price FROM 
Prices p LEFT JOIN UnitsSold u ON p.product_id = u.product_id AND
u.purchase_date between p.start_date AND p.end_date group by p.product_id;