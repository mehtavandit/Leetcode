# Write your MySQL query statement below
SELECT
    c.name as Customers
FROM Customers as c
LEFT JOIN Orders o on c.id = o.customerID
where o.customerID is NULL;