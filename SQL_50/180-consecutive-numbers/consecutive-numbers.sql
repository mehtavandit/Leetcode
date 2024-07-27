# Write your MySQL query statement below
SELECT DISTINCT table1.num as ConsecutiveNums
FROM logs table1 
JOIN logs table2 ON table1.id = table2.id + 1 AND table1.num = table2.num 
JOIN logs table3 ON table1.id = table3.id + 2 AND table1.num = table3.num;
