-- Problem: Big Countries
-- Language: mysql
-- Runtime: 275 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT name, population, area FROM World
WHERE area >= 3000000 OR population >= 25000000