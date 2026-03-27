-- Problem: The Number of Employees Which Report to Each Employee
-- Language: mysql
-- Runtime: 1083 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT e1.employee_id, 
       e1.name,
       COUNT(DISTINCT e2.employee_id) AS reports_count,
       ROUND(AVG(e2.age)) AS average_age
FROM Employees e1
INNER JOIN Employees e2 ON e2.reports_to = e1.employee_id
GROUP BY 1,2
ORDER BY 1