-- Problem: Leetflex Banned Accounts
-- Language: mysql
-- Runtime: 587 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT DISTINCT l1.account_id
FROM LogInfo l1
INNER JOIN LogInfo l2 ON l1.account_id = l2.account_id and l1.ip_address != l2.ip_address 
WHERE l1.login <= l2.login AND l2.login <= l1.logout
