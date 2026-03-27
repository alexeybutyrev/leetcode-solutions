-- Problem: Combine Two Tables
-- Language: mysql
-- Runtime: 315 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId