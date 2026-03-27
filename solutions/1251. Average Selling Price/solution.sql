-- Problem: Average Selling Price
-- Language: mysql
-- Runtime: 723 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT  
       u.product_id,
       ROUND(SUM(dollars) / SUM(counts),2) AS average_price
FROM (
    SELECT u.product_id,
           u.purchase_date,
           p.price * units AS dollars,
           units AS counts
    FROM UnitsSold u
    INNER JOIN Prices p ON p.product_id = u.product_id
    WHERE u.purchase_date >= start_date AND u.purchase_date <= end_date
    GROUP BY 1,2
) u
#WHERE product_id=2
GROUP BY 1