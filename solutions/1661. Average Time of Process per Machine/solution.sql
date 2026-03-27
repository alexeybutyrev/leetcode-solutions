-- Problem: Average Time of Process per Machine
-- Language: mysql
-- Runtime: 393 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT x.machine_id,
       ROUND(AVG(end_time - start_time),3) AS processing_time
FROM (
    SELECT s.machine_id,
           s.process_id,
           s.timestamp AS start_time,
           e.ts AS end_time
    FROM Activity s
    INNER JOIN (
        SELECT machine_id,
           process_id,
           timestamp AS ts
        FROM Activity
        WHERE activity_type = 'end'
    ) e ON (e.process_id = s.process_id AND e.machine_id = s.machine_id)
    WHERE activity_type = 'start'
) x
GROUP BY 1