# Write your MySQL query statement below
select table1.customer_id, count(*) as count_no_trans from Visits table1 Left join Transactions table2 
on table1.visit_id = table2.visit_id where table2.transaction_id is null group by table1.customer_id;