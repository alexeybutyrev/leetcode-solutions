-- Problem: Nth Highest Salary
-- Language: mysql
-- Runtime: 307 ms
-- Memory: 0.0B

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT CASE WHEN cnt = N THEN S
             ELSE NULL
             END AS Salary
      FROM (
      
          SELECT COUNT(*) AS cnt,
                 MIN(Salary) AS S
          FROM (
              SELECT DISTINCT Salary 
              FROM Employee
              ORDER BY 1 DESC
              LIMIT N ) x 
    ) y
      
      
  );
END