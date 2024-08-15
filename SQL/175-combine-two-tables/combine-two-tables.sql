# Write your MySQL query statement below
SELECT
    p.firstName, p.lastName, a.city, a.state
FROM
    person as p
LEFT JOIN address as a
ON
    p.personId = a.personId;