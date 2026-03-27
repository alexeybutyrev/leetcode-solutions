-- Problem: Managers with at Least 5 Direct Reports
-- Language: mysql
-- Runtime: 311 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT DISTINCT name
FROM Employee n
INNER JOIN ( 
    SELECT managerId, COUNT(*)
    FROM Employee
    WHERE managerID <> 'None'
    GROUP BY 1
    HAVING COUNT(*) > 4
) m ON m.managerId = n.id