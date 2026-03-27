-- Problem: Find the Team Size
-- Language: mysql
-- Runtime: 341 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT employee_id, team_size 
FROM Employee e
INNER JOIN (
    SELECT team_id, COUNT(*) AS team_size
    FROM Employee
    GROUP BY 1
) s ON s.team_id = e.team_id

