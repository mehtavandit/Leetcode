# Write your MySQL query statement below
select x,y,z,
CASE when x+y>z and x+z>y AND y+z>x then 'Yes' ELSE 'No' END as triangle from triangle;