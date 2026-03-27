-- Problem: Monthly Transactions I
-- Language: mysql
-- Runtime: 666 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT 
       DATE_FORMAT(trans_date, "%Y-%m") AS month,
       country,
       COUNT(*) AS trans_count,
       SUM(amount) AS trans_total_amount,
       IFNULL(COUNT(DISTINCT CASE WHEN state = 'approved' THEN id ELSE NULL END),0) AS approved_count,
       IFNULL(SUM(CASE WHEN state = 'approved' THEN amount ELSE NULL END),0) AS approved_total_amount
       
FROM Transactions
GROUP BY 1,2