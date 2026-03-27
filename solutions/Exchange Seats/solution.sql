-- Problem: Exchange Seats
-- Language: mysql
-- Runtime: 251 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT 
       IFNULL(s2.id,s1.id) AS id,
       CASE WHEN s2.id IS NULL THEN s1.student ELSE s2.student END AS student
FROM Seat s1
LEFT JOIN (
    SELECT id-1 AS id,
           student
    FROM Seat
    WHERE id % 2 = 0
) s2 ON s1.id = s2.id
WHERE IFNULL(s2.id,s1.id) % 2 <> 0

UNION 
SELECT s2.id, 
       s2.student
FROM Seat s1
INNER JOIN (
    SELECT id+1 AS id,
           student
    FROM Seat
    WHERE id % 2 <> 0
) s2 ON s1.id = s2.id
ORDER BY 1