# Write your MySQL query statement below
Select E1.name 
from Employee E1
Join (
    select managerID , count(*) as directReports from Employee group by managerID Having count(*) >=5
) E2 on E1.id = E2.managerId;