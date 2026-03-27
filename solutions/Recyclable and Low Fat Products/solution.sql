-- Problem: Recyclable and Low Fat Products
-- Language: mysql
-- Runtime: 906 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT product_id FROM Products
WHERE low_fats = "Y" AND recyclable = "Y"