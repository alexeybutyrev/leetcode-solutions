-- Problem: Department Highest Salary
-- Language: mysql
-- Runtime: 630 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT d.name AS Department,
       e.name AS Employee,
       e.salary AS Salary
FROM Employee e       
INNER JOIN (
    SELECT departmentId,
           MAX(Salary) AS Salary
    FROM Employee e
    GROUP BY 1
) m ON m.salary = e.salary AND e.departmentId = m.departmentId
INNER JOIN Department d ON d.id = e.departmentId
