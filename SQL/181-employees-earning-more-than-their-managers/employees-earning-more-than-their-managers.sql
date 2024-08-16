# Write your MySQL query statement below
select e1.name as Employee
from Employee e1 INNER JOIN Employee e2 ON e1.managerID = e2.id
where e1.salary > e2.salary;