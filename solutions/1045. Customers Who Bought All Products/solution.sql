-- Problem: Customers Who Bought All Products
-- Language: mysql
-- Runtime: 447 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT customer_id
FROM Customer
GROUP BY 1
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(DISTINCT product_key) FROM Customer)