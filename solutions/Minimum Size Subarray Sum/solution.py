# Problem: Minimum Size Subarray Sum
# Language: python3
# Runtime: 84 ms
# Memory: 16.8 MB

from bisect import bisect_right
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        
        prefix = [0]
        for a in nums:
            prefix.append(prefix[-1] + a)
        
        
        
        
        l = inf
        N = len(prefix)
        
        """ 
        for i in range(N):
            for j in range(i+1, N):
                if prefix[j] - prefix[i] >= target:
                    l = min(l, j - i)
                    print(i, j, l)
        
        return l
        """
        
        for i,a in enumerate(prefix):
            j = bisect_right(prefix, a + target)
            
            if j < N:
                if j > 0 and prefix[j - 1] >= a + target:
                    l = min(l, j - i - 1)
                else:
                    l = min(l, j - i)
            else:
                if prefix[N-1] >= a + target:
                    l = min(l, N - 1 - i)
        return 0 if l == inf else l