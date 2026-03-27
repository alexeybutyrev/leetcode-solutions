-- Problem: Actors and Directors Who Cooperated At Least Three Times
-- Language: mysql
-- Runtime: 699 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY 1,2
HAVING COUNT(*) > 2