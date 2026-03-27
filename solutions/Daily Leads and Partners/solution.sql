-- Problem: Daily Leads and Partners
-- Language: mysql
-- Runtime: 567 ms
-- Memory: 0 MB

# Write your MySQL query statement below
SELECT date_id, 
       make_name, 
       COUNT(DISTINCT lead_id) AS unique_leads,
       COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY 1,2
