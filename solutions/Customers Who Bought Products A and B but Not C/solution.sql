-- Problem: Customers Who Bought Products A and B but Not C
-- Language: mysql
-- Runtime: 733 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT DISTINCT a.customer_id,
       n.customer_name
FROM Orders a
INNER JOIN (SELECT DISTINCT customer_id FROM Orders WHERE product_name = 'B') b ON b.customer_id = a.customer_id
LEFT JOIN (SELECT DISTINCT customer_id FROM Orders WHERE product_name = 'C') c ON c.customer_id = b.customer_id
INNER JOIN Customers n ON n.customer_id = a.customer_id
WHERE a.product_name = 'A' AND c.customer_id IS NULL
ORDER BY 1