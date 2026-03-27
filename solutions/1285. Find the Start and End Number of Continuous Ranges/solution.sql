-- Problem: Find the Start and End Number of Continuous Ranges
-- Language: mysql
-- Runtime: 361 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT start_id, end_id FROM
(
    SELECT diff_rnk,
           MIN(log_id) AS start_id,
           MAX(log_id) AS end_id
    FROM (
    SELECT log_id,(log_id-ROW_NUMBER() OVER(ORDER BY log_id ASC)) AS diff_rnk FROM Logs
    ) x
    GROUP BY 1
) y