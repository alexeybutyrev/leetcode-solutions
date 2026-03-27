-- Problem: Project Employees III
-- Language: mysql
-- Runtime: 733 ms
-- Memory: 0.0B

# Write your MySQL query statement below

WITH epe AS 
(
SELECT 
       project_id,
       MAX(experience_years) AS mx
FROM Employee e
INNER JOIN Project p ON p.employee_id = e.employee_id
GROUP BY 1
)

SELECT e.employee_id, 
       p.project_id
FROM Employee e
INNER JOIN Project p ON p.employee_id = e.employee_id
INNER JOIN epe ep ON ep.project_id = p.project_id AND ep.mx = e.experience_years


