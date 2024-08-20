# Write your MySQL query statement below
SELECT
    u.name as Name,sum(t.amount) as balance
FROM Users as u
INNER JOIN Transactions as t
ON u.account = t.account
group by u.account
HAVING 
    SUM(t.amount) > 10000;