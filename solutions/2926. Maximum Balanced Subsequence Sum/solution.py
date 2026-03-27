# Problem: Maximum Balanced Subsequence Sum
# Language: python3
# Runtime: 1117 ms
# Memory: 38.7 MB

class Solution:
    def maxBalancedSubsequenceSum(self, A: List[int]) -> int:
        N = len(A)
        keys = {(x-i) for i,x in enumerate(A) if x > 0}
        
        if not keys: return max(A)
        N = len(keys)
        
        hm = {x: i for i,x in enumerate(sorted(keys))}
        BIT = [0] * (N+1)
        
        def count(x):
            s = 0
            while x:
                s = max(s,BIT[x])
                x -= (x & -x)
            return s
        
        def update(x,y):
            while x < N + 1:
                BIT[x] = max(BIT[x],y)
                x += x & -x

        ans = 0
        for i,x in enumerate(A):
            if x > 0:
                key = hm[x-i] + 1
                s = count(key)
                s += x
                update(key, s)
            
        return max(BIT)
        #for x,i in A:
            