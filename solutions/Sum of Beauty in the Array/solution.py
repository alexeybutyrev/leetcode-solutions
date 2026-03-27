# Problem: Sum of Beauty in the Array
# Language: python3
# Runtime: 1160 ms
# Memory: 42 MB

class Solution:
    def sumOfBeauties(self, A: List[int]) -> int:
        mins = {}
        maxs = {}
        
        N = len(A)
        mn = A[0]
        for i in range(1,N):
            mins[i] = mn
            mn = max(A[i],mn)
        
        mx = A[N-1]
        for i in range(N-1,0,-1):
            maxs[i] = mx
            mx = min(A[i],mx)
        

        ans = 0
        for i in range(1,N-1):
            if mins[i] < A[i] < maxs[i]:
                ans += 2
            elif A[i-1] < A[i] < A[i+1]:
                ans += 1
        
        return ans
        