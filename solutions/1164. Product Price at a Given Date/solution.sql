-- Problem: Product Price at a Given Date
-- Language: mysql
-- Runtime: 660 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT p.product_id,
       new_price AS price
FROM Products p 
INNER JOIN (
    SELECT product_id, 
           MAX(change_date) AS dt
    FROM Products
    WHERE change_date <= "2019-08-16"
    GROUP BY 1
) cd ON p.product_id = cd.product_id AND dt = change_date
UNION 
SELECT DISTINCT p.product_id,
       10 AS price
FROM Products p 
INNER JOIN (
    SELECT product_id, 
           MIN(change_date) AS dt
    FROM Products
    GROUP BY 1
) cd ON p.product_id = cd.product_id
WHERE dt > '2019-08-16'