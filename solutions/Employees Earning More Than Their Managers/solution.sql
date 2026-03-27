-- Problem: Employees Earning More Than Their Managers
-- Language: mysql
-- Runtime: 370 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT e.Name AS Employee
FROM Employee e
INNER JOIN Employee m ON m.id = e.ManagerId
WHERE m.Salary < e.Salary