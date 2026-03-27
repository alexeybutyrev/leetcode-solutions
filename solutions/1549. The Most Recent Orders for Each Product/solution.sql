-- Problem: The Most Recent Orders for Each Product
-- Language: mysql
-- Runtime: 3119 ms
-- Memory: 0.0B

# Write your MySQL query statement below

SELECT a.product_name,a.product_id, b.order_id, a.od as order_date FROM(
(SELECT p.product_id, p.product_name, MAX(o.order_date) as od FROM Products p
INNER JOIN Orders o
using(product_id)
group by 1,2)a
JOIN
(SELECT product_id, order_id, MAX(order_date) as od FROM Orders
group by 1,2 )b
on a. product_id = b.product_id and a.od = b.od
    )
    ORDER BY 1,3
