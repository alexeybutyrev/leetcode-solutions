-- Problem: Rank Scores
-- Language: mysql
-- Runtime: 478 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT score,
       DENSE_RANK() OVER(ORDER BY score DESC) AS `rank`
FROM Scores