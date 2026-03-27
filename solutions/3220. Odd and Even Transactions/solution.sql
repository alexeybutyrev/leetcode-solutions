-- Problem: Odd and Even Transactions
-- Language: mysql
-- Runtime: 292 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT transaction_date, 
      SUM(amount * MOD(amount,2)) AS odd_sum, 
      SUM(amount * (MOD(amount,2) = 0)) AS even_sum
FROM transactions
GROUP BY 1
ORDER BY 1 ASC