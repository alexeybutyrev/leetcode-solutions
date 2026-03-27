-- Problem: Count Student Number in Departments
-- Language: mysql
-- Runtime: 1051 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT dept_name, COUNT(DISTINCT s.student_id) AS student_number
FROM Department d
LEFT JOIN Student s ON s.dept_id = d.dept_id
GROUP BY 1
ORDER BY 2 DESC