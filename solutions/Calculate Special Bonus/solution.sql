-- Problem: Calculate Special Bonus
-- Language: mysql
-- Runtime: 553 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT employee_id,
       CASE WHEN name LIKE 'M%' or 0 = employee_id % 2 THEN 0
            ELSE salary END AS bonus
FROM Employees
ORDER BY 1