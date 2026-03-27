# Problem: Paint House II
# Language: python3
# Runtime: 108 ms
# Memory: 14.4 MB

from copy import deepcopy
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        N = len(costs)
        k = len(costs[0])
        prev = costs[0]
        
        for i in range(1,N):
            curr = costs[i]
            for j in range(k):
                curr[j] += min(prev[:j] + prev[j+1:])
            prev = curr
        
        return min(prev)