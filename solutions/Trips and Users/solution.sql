-- Problem: Trips and Users
-- Language: mysql
-- Runtime: 575 ms
-- Memory: 0 MB

SELECT Request_at AS Day, 
       ROUND(1.0 * SUM(Status IN ('cancelled_by_driver','cancelled_by_client')) / COUNT(*),2) AS `Cancellation Rate`
FROM Trips t
INNER JOIN Users ud ON t.Driver_Id = ud.Users_Id
INNER JOIN Users uc ON t.Client_Id = uc.Users_Id
WHERE ud.Banned = 'No' AND uc.Banned = 'No'
AND Request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY Request_at


#
#SELECT 1.0 * SUM(Status IN ('cancelled_by_driver','cancelled_by_client')) / COUNT(*)
#FROM Trips 
#INNER JOIN Users uc ON t.Client_Id = uc.Users_Id
#INNER JOIN Users ud ON t.Driver_Id = ud.Users_Id
#
#