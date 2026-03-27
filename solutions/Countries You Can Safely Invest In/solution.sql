-- Problem: Countries You Can Safely Invest In
-- Language: mysql
-- Runtime: 944 ms
-- Memory: 0 MB

# Write your MySQL query statement below
WITH person_cc_code AS (
    SELECT id, LEFT(phone_number,3) AS cc
    FROM Person
),
tot_calls AS (
    SELECT AVG(duration) AS duration
    FROM Calls
),
avg_calls AS (
    SELECT cc, AVG(duration) AS duration
    FROM person_cc_code
    INNER JOIN Calls ON callee_id = id OR id = caller_id
    GROUP BY 1
    HAVING AVG(duration) > (SELECT duration FROM tot_calls)
)

SELECT name AS country FROM avg_calls a
INNER JOIN Country c ON c.country_code = a.cc