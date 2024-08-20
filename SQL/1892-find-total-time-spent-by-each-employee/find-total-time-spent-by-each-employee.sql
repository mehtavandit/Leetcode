# Write your MySQL query statement below
WITH TEMP AS(
    SELECT
    emp_id,
    event_day,
    out_time - in_time as total_time_per_event
    FROM Employees
)

SELECT
    event_day as day,
    emp_id,
    SUM(total_time_per_event) as total_time
FROM temp
GROUP BY event_day, emp_id;