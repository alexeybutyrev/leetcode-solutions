# Problem: Gas Station
# Language: python3
# Runtime: 52 ms
# Memory: 14.9 MB

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        cur_tank = 0
        start_station = 0
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            cur_tank += gas[i] - cost[i]
            
            if cur_tank < 0:
                cur_tank  = 0
                start_station = i + 1
        
        return start_station if total_tank >= 0 else -1
    
                
                