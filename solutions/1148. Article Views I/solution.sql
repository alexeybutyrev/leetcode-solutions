-- Problem: Article Views I
-- Language: mysql
-- Runtime: 581 ms
-- Memory: 0.0B

# Write your MySQL query statement below
SELECT DISTINCT author_id AS id
FROM Views v
WHERE v.author_id = viewer_id
ORDER BY 1