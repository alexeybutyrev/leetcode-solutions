-- Problem: Game Play Analysis IV
-- Language: mysql
-- Runtime: 729 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT ROUND(COUNT(DISTINCT a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity),2) AS fraction
FROM (
    SELECT player_id, 
           MIN(event_date) AS login_date
    FROM Activity 
    GROUP BY 1
)  a
INNER JOIN Activity aft ON (a.login_date + 1 = aft.event_date) AND aft.player_id = a.player_id

