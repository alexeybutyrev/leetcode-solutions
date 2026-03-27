-- Problem: Immediate Food Delivery I
-- Language: mysql
-- Runtime: 903 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT ROUND(IFNULL(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END),0) * 100 / (SELECT COUNT(*) FROM Delivery),2) AS immediate_percentage
FROM Delivery