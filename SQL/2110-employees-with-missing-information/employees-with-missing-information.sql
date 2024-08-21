# Write your MySQL query statement below
WITH TEMP AS(SELECT e.employee_id
FROM Employees E
LEFT JOIN Salaries s
ON e.employee_id = s.employee_id
where s.salary is null

UNION ALL

SELECT s.employee_id
FROM Employees E
RIGHT JOIN Salaries s
ON e.employee_id = s.employee_id
where e.name is null)

select * from temp order by employee_id;