-- Problem: Find Followers Count
-- Language: mysql
-- Runtime: 539 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT user_id, COUNT(DISTINCT follower_id) AS followers_count
FROM Followers
GROUP BY 1
ORDER BY 1