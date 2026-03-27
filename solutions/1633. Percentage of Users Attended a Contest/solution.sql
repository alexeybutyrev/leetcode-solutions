-- Problem: Percentage of Users Attended a Contest
-- Language: mysql
-- Runtime: 1063 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT contest_id,
       ROUND(COUNT(DISTINCT user_id) * 100 / (SELECT COUNT(DISTINCT user_id) FROM Users),2) AS percentage
FROM Register
GROUP BY 1
ORDER BY 2 DESC, 1