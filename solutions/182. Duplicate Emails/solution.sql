-- Problem: Duplicate Emails
-- Language: mysql
-- Runtime: 477 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT email
FROM (
    SELECT email, COUNT(*) AS cnt FROM Person
    GROUP BY 1
) e
WHERE cnt > 1