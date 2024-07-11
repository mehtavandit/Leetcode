# Write your MySQL query statement below
select w2.id as ID from Weather w1 Join Weather w2 on DATEDIFF(w1.recordDate, w2.recordDate) = -1 where w2.temperature > w1.temperature;
