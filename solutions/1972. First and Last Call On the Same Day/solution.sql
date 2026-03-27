-- Problem: First and Last Call On the Same Day
-- Language: mysql
-- Runtime: 398 ms
-- Memory: 0.0B

# Write your MySQL query statement below
WITH cc AS (
    SELECT caller_id,
           recipient_id,
           call_time
    FROM Calls
    UNION 
    SELECT recipient_id AS caller_id,
           caller_id AS recipient_id,
           call_time
    FROM Calls
),
fl_call AS (
SELECT caller_id,
       DATE(call_time) AS day,
       MIN(call_time)  AS last_call,
       MAX(call_time)  AS first_call
FROM cc c
GROUP BY 1,2
),
first_call AS (
SELECT c.caller_id,
       recipient_id,
       DATE(call_time) AS day
FROM cc c
INNER JOIN fl_call f ON f.first_call = c.call_time AND f.caller_id = c.caller_id
),
last_call AS (
SELECT c.caller_id,
       recipient_id,
       DATE(call_time) AS day
FROM cc c
INNER JOIN fl_call f ON f.last_call = c.call_time AND f.caller_id = c.caller_id
)
SELECT DISTINCT l.caller_id AS user_id
FROM first_call f
INNER JOIN last_call l ON l.caller_id = f.caller_id and f.recipient_id = l.recipient_id
