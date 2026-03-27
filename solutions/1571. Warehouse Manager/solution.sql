-- Problem: Warehouse Manager
-- Language: mysql
-- Runtime: 1028 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT name AS warehouse_name, SUM(Width*Length*Height*units) AS volume
FROM Warehouse w
INNER JOIN Products p ON p.product_id = w.product_id
GROUP BY 1