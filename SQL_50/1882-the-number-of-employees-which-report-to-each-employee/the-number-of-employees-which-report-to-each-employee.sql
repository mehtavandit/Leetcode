# Write your MySQL query statement below
select e1.employee_id, e1.name, count(e2.reports_to) as reports_count, Round(avg(e2.age))
as average_age from employees e1
RIGHT JOIN employees e2 on e1.employee_id = e2.reports_to where e1.employee_id is Not Null
group by e1.employee_id order by e1.employee_id;