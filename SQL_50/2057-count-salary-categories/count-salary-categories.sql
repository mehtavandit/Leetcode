# Write your MySQL query statement below
SELECT
    'Low Salary' as category,
    count(*) as accounts_count
FROM Accounts
where 
    income < 20000

UNION ALL

SELECT
    'Average Salary' as category,
    count(*) as accounts_count
FROM Accounts
where 
    income BETWEEN 20000 and 50000

UNION ALL

SELECT
    'High Salary' as category,
    count(*) as accounts_count
FROM Accounts
where 
    income > 50000;
