# Problem: Minimum Operations to Make a Subsequence
# Language: python3
# Runtime: 1080 ms
# Memory: 46.7 MB

from bisect import bisect_left
from collections import defaultdict
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        N = len(arr)
        
        dp = [-1]
        
        hm = defaultdict(list)
        for i,a in enumerate(arr):
            hm[a].append(i)
        
        l = 0
        for a in target:
            if a in hm:
                for r in reversed(hm[a]):
                    ind = bisect_left(dp, r)
                    if ind >= len(dp):
                        dp.append(-1)
                    dp[ind] = r
        
        return len(target) - len(dp) + 1