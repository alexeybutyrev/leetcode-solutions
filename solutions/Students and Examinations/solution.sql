-- Problem: Students and Examinations
-- Language: mysql
-- Runtime: 698 ms
-- Memory: 0 MB

# Write your MySQL query statement below
WITH cj AS (
    SELECT DISTINCT student_id,
                    student_name,
                    subject_name
    FROM Students j
    CROSS JOIN Subjects
)
SELECT cj.student_id, 
       cj.student_name,
       cj.subject_name,
       SUM(CASE WHEN e.subject_name IS NULL THEN 0 ELSE 1 END) AS attended_exams
FROM cj 
LEFT JOIN (
    SELECT s.student_id, student_name, subject_name FROM Examinations e
    INNER JOIN Students s ON s.student_id = e.student_id
) e ON cj.subject_name = e.subject_name AND cj.student_id = e.student_id
GROUP BY 1,2,3
ORDER BY 1,3
