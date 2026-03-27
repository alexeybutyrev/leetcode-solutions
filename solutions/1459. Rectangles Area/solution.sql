-- Problem: Rectangles Area
-- Language: mysql
-- Runtime: 355 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT p1.id AS P1,
       p2.id AS P2,
       abs(p1.x_value - p2.x_value) * abs(p1.y_value - p2.y_value) AS AREA
FROM Points AS p1
INNER JOIN Points AS p2 ON p1.x_value != p2.x_value AND p1.y_value != p2.y_value AND p1.id < p2.id
ORDER BY 3 DESC,1,2