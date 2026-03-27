-- Problem: Department Top Three Salaries
-- Language: mysql
-- Runtime: 625 ms
-- Memory: 0.0B

# Write your MySQL query statement below
WITH ranked AS (
     SELECT id, 
            name, 
            departmentId, 
            salary,
            DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS rr
    FROM Employee 

) 

SELECT d.name AS Department, 
       r.name AS Employee,
       salary
FROM ranked r
INNER JOIN Department d ON d.id = r.departmentId
WHERE rr <= 3