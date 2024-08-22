# Write your MySQL query statement below
WITH TEMP AS(
    SELECT
        d.name as Department, e.name as Employee, e.salary as Salary, DENSE_RANK() OVER(PARTITION BY e.departmentID ORDER BY e.salary DESC) as status
    FROM Employee as e
    INNER JOIN Department as d 
    ON e.departmentID = d.id
)

SELECT Department, Employee, Salary from temp where status = 1;