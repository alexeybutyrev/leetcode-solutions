-- Problem: Highest Grade For Each Student
-- Language: mysql
-- Runtime: 556 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT e.student_id,
       MIN(e.course_id) AS course_id,
       e.grade 
       
FROM Enrollments e
INNER JOIN (
    SELECT student_id,
           MAX(grade) AS grade
    FROM Enrollments e
GROUP BY 1) mx ON mx.student_id = e.student_id AND mx.grade = e.grade
GROUP BY 1,3
ORDER BY 1