# Write your MySQL query statement below
select r.contest_id, ROUND(COUNT(DISTINCT R.user_id)/COUNT(DISTINCT U.user_id) * 100, 2) as percentage from Users U
JOIN Register R  group by r.contest_id order by percentage DESC, r.contest_id;