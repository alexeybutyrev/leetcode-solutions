-- Problem: The Most Frequently Ordered Products for Each Customer
-- Language: mysql
-- Runtime: 2110 ms
-- Memory: 0.0B

# Write your MySQL query statement below
WITH prods AS 

(SELECT customer_id, 
       product_id,
       COUNT(*) AS cnt
 FROM Orders
 GROUP BY 1,2
 ),
 mx AS (
     SELECT customer_id,
            MAX(cnt) AS mx
     FROM prods
     GROUP BY 1
 )
SELECT  p.customer_id,
        p.product_id,
        product_name
FROM prods p
INNER JOIN mx m ON m.customer_id = p.customer_id and p.cnt = m.mx
INNER JOIN Products pn ON pn.product_id = p.product_id

 