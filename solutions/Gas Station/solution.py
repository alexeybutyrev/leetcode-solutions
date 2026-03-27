# Problem: Gas Station
# Language: python3
# Runtime: 48 ms
# Memory: 15.2 MB

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total_tank = 0
        curr_tank   = 0
        
        ans = 0
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            
            if curr_tank < 0:
                curr_tank = 0
                ans = i + 1
        
        return ans if total_tank >= 0 else -1