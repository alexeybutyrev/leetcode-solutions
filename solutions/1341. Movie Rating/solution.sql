-- Problem: Movie Rating
-- Language: mysql
-- Runtime: 1051 ms
-- Memory: 0.0B

# Write your MySQL query statement below
WITH r AS (
  SELECT user_id, COUNT(*) AS cnt
  FROM MovieRating r
  GROUP BY 1
),
rx AS (
  SELECT movie_id, AVG(rating) AS cnt
  FROM MovieRating r
  WHERE YEAR(created_at) = 2020 AND MONTH(created_at) = 2
  GROUP BY 1
)
SELECT * FROM (
    SELECT MIN(u.name) AS results
    FROM r rt
    INNER JOIN ( SELECT MAX(cnt) AS cnt FROM r ) mx ON rt.cnt = mx.cnt
    INNER JOIN Users u ON rt.user_id = u.user_id

    UNION ALL
    
    SELECT MIN(u.title) AS results
    FROM rx rt
    INNER JOIN ( SELECT MAX(cnt) AS cnt FROM rx ) mx ON rt.cnt = mx.cnt
    INNER JOIN Movies u ON rt.movie_id = u.movie_id
) x
# cnt = ()