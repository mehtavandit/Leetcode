# Write your MySQL query statement below
select DATE_FORMAT(trans_date, '%Y-%m') as  month,
country,
count(id) as trans_count,
SUM(CASE when state = 'approved' THEN 1 ELSE 0 END) as approved_count,
SUM(amount) AS trans_total_amount,
SUM(CASE when state='approved' THEN amount else 0 END) as approved_total_amount
from Transactions group by month, country;