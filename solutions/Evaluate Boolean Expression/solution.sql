-- Problem: Evaluate Boolean Expression
-- Language: mysql
-- Runtime: 971 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT left_operand,operator,right_operand,
        CASE WHEN operator = ">" THEN IF(lv.value > rv.value, 'true', 'false')
            WHEN operator = "<" THEN IF(lv.value < rv.value, 'true', 'false')
            ELSE IF(lv.value = rv.value, 'true', 'false') END AS value
FROM Expressions e
INNER JOIN Variables lv ON lv.name =  e.left_operand
INNER JOIN Variables rv ON rv.name =  e.right_operand
