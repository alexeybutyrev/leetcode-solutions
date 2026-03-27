-- Problem: Department Highest Salary
-- Language: mysql
-- Runtime: 590 ms
-- Memory: 0 MB

# Write your MySQL query statement below

SELECT dn.Name AS Department,
       e.Name  AS Employee,
       e.Salary AS Salary
FROM Employee e
INNER JOIN (
    SELECT  DepartmentId,
            MAX(Salary) AS Salary
    FROM Employee d
    GROUP BY DepartmentId
) s ON (s.DepartmentId = e.DepartmentId AND s.Salary = e.Salary)
INNER JOIN Department dn ON e.DepartmentId = dn.Id