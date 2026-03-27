-- Problem: Find Cutoff Score for Each School
-- Language: mysql
-- Runtime: 839 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT school_id,
       IFNULL(MIN(score),-1) AS score
       
FROM Schools s
LEFT JOIN Exam e ON e.student_count <= s.capacity
GROUP BY 1