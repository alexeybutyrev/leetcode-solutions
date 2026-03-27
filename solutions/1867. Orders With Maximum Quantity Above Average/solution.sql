-- Problem: Orders With Maximum Quantity Above Average
-- Language: mysql
-- Runtime: 927 ms
-- Memory: 0.0B

# Write your MySQL query statement below
Select order_id
from
(
Select avg(quantity) a, max(quantity) m, order_id
from OrdersDetails
group by order_id
) t
where m > all ( Select avg(quantity) from OrdersDetails group by order_id)