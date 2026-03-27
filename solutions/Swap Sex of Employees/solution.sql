-- Problem: Swap Sex of Employees
-- Language: mysql
-- Runtime: 214 ms
-- Memory: 0 MB

# Write your MySQL query statement below

UPDATE `Salary` SET `sex` = CASE WHEN sex = 'f' THEN 'm' ELSE 'f' END
