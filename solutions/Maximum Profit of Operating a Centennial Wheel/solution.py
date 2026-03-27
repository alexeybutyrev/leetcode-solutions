# Problem: Maximum Profit of Operating a Centennial Wheel
# Language: python3
# Runtime: 5368 ms
# Memory: 17.8 MB

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        n = len(customers)
        max_profit = -1
        waiting = 0
        total_people = 0
        i = 0
        ind = -1
        while customers or waiting > 0:
            i+=1
            if customers:
                curr = customers.pop(0)    
                waiting += curr
                
            if waiting >= 4:
                to_sit = 4
                waiting -= 4
            else:
                to_sit = waiting
                waiting = 0
            
            total_people += to_sit
            profit = total_people * boardingCost - i * runningCost
            if profit > max_profit:
                ind = i
                max_profit = profit
        
        return ind