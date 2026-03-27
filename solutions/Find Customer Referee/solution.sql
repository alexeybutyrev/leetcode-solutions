-- Problem: Find Customer Referee
-- Language: mysql
-- Runtime: 580 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT name FROM Customer
WHERE referee_id IS NULL OR referee_id <> 2