-- Problem: Weather Type in Each Country
-- Language: mysql
-- Runtime: 623 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT country_name,
       CASE WHEN weather_state <= 15 THEN "Cold"
            WHEN weather_state >= 25 THEN "Hot"
            ELSE "Warm"
       END AS weather_type
FROM 
(
    SELECT country_id, AVG(weather_state) AS weather_state 
    FROM Weather w
    WHERE YEAR(day) = 2019 AND MONTH(day)= 11
    GROUP BY 1
) w
INNER JOIN Countries c ON c.country_id = w.country_id
