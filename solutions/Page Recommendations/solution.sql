-- Problem: Page Recommendations
-- Language: mysql
-- Runtime: 609 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT DISTINCT l2.page_id AS recommended_page
FROM 
(
SELECT * FROM Friendship 
UNION 
    SELECT user2_id AS user1_id,
           user1_id AS user2_id
    FROM Friendship 
)f2
INNER JOIN Likes l2 ON user2_id = user_id
LEFT JOIN (SELECT DISTINCT page_id FROM Likes WHERE user_id = 1) u1 ON u1.page_id = l2.page_id
WHERE user1_id = 1 AND u1.page_id IS NULL