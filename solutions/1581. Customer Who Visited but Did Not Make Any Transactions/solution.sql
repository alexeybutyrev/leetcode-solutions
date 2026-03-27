-- Problem: Customer Who Visited but Did Not Make Any Transactions
-- Language: mysql
-- Runtime: 1220 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT v.customer_id, 
       COUNT(*) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t ON (v.visit_id = t.visit_id)
WHERE t.visit_id IS NULL
GROUP BY 1
