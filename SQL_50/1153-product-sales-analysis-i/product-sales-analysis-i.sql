# Write your MySQL query statement below
select table2.product_name, table1.year, table1.price from Product table2 Join Sales table1 on table2.product_id = table1.product_id;