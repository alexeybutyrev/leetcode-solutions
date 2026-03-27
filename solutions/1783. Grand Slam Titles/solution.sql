-- Problem: Grand Slam Titles
-- Language: mysql
-- Runtime: 3231 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT player_id,
       player_name,
       COUNT(*) AS grand_slams_count
FROM (
    SELECT Wimbledon as id
    FROM Championships
    UNION ALL
    SELECT Fr_open as id
    FROM Championships
    UNION ALL
    SELECT US_open as id
    FROM Championships
    UNION ALL
    SELECT Au_open as id
    FROM Championships
) ids 
INNER JOIN Players p ON p.player_id = ids.id
GROUP BY 1,2