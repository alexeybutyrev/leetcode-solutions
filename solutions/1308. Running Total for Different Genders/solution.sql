-- Problem: Running Total for Different Genders
-- Language: mysql
-- Runtime: 1321 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT gender,
       day,
       SUM(score_points) OVER(PARTITION BY gender ORDER BY day) AS total
FROM Scores
ORDER BY 1,2