-- Problem: Apples & Oranges
-- Language: mysql
-- Runtime: 331 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT a.sale_date,
       sold_num - oranges AS diff
FROM Sales a 
INNER JOIN (
    SELECT sale_date,
           sold_num AS oranges
    FROM Sales
    WHERE fruit = 'oranges'
) o ON o.sale_date = a.sale_date
WHERE fruit = 'apples'