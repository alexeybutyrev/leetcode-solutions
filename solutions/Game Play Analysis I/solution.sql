-- Problem: Game Play Analysis I
-- Language: mysql
-- Runtime: 1273 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY 1