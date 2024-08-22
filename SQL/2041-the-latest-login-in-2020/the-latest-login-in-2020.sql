SELECT  
    user_id, MAX(time_stamp) as last_stamp
FROM logins 
where YEAR(time_stamp) = 2020
GROUP BY user_id;