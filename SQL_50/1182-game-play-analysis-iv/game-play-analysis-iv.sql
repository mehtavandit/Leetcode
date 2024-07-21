With temp as (
    select player_id, min(event_date) as first_login_date
    from activity
    group by player_id
)

SELECT
    ROUND(
        SUM(CASE WHEN DATEDIFF(a.event_date, t.first_login_date) = 1 THEN 1 ELSE 0 END) / 
        NULLIF(COUNT(DISTINCT a.player_id), 0), 
        2
    ) AS fraction
FROM
    Activity a
JOIN
    temp t
ON
    a.player_id = t.player_id;
