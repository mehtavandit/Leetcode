# Write your MySQL query statement below
WITH TEMP1 AS (
    SELECT tiv_2015 FROM Insurance GROUP BY tiv_2015 HAVING COUNT(*) > 1
),
TEMP2 AS(
    SELECT LAT, LON 
    FROM Insurance 
    GROUP BY LAT, LON 
    HAVING COUNT(*) = 1
)

select ROUND(SUM(tiv_2016), 2) as tiv_2016 from insurance 
where tiv_2015 IN (select * from temp1)
and (lat, lon) IN (select * from temp2);