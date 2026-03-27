-- Problem: Consecutive Available Seats
-- Language: mysql
-- Runtime: 593 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT DISTINCT seat_id 
FROM
(
    SELECT c1.seat_id
    FROM Cinema c1
    INNER JOIN Cinema c2 ON c1.seat_id = c2.seat_id + 1
    WHERE c1.free = 1 and c2.free = 1
    UNION ALL
    SELECT c1.seat_id
    FROM Cinema c1
    INNER JOIN Cinema c2 ON c1.seat_id = c2.seat_id - 1
    WHERE c1.free = 1 and c2.free = 1
) x
ORDER BY 1