-- Problem: Find the Subtasks That Did Not Execute
-- Language: mysql
-- Runtime: 850 ms
-- Memory: 0.0B

# Write your MySQL query statement below
WITH recursive stask_id AS (

SELECT 1 AS id,
       0 AS k
UNION 
SELECT id + 1, 0 AS k
FROM stask_id
WHERE id < (SELECT MAX(subtasks_count) FROM Tasks)
)
SELECT t2.task_id, id AS subtask_id FROM stask_id s
INNER JOIN ( SELECT DISTINCT task_id, 0 AS k FROM Tasks t ) t2 ON t2.k = s.k
INNER JOIN Tasks t3 ON t3.task_id = t2.task_id AND s.id <= t3.subtasks_count
LEFT JOIN Executed e ON e.task_id = t2.task_id AND e.subtask_id = s.id
WHERE e.subtask_id IS NULL
ORDER BY 1,2

