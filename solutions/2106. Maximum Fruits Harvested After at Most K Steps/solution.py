# Problem: Maximum Fruits Harvested After at Most K Steps
# Language: python3
# Runtime: 3932 ms
# Memory: 96 MB

from sortedcontainers import SortedList
class Solution:
    def maxTotalFruits(self, A: List[List[int]], start: int, K: int) -> int:
        pre = defaultdict(int)
        M = max(A[-1][0], start + K)
        
        for x,v in A:
            pre[x] += v
        
        for i in range(1,M+1):
            pre[i] += pre[i-1]
        
        ans = 0 
        
        for i in range((K+1) // 2 + 1):
            lo = start - i
            hi = start + K - 2 * i
            
            count = pre[hi] - pre[lo-1]
            ans = max(ans,count)
            
            lo = start - (K - 2 * i)
            hi = start + i
            
            count = pre[hi] - pre[lo-1]
            ans = max(ans,count)
            
            
        
        return ans