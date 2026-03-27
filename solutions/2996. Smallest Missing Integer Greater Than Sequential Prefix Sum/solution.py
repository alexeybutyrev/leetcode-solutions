# Problem: Smallest Missing Integer Greater Than Sequential Prefix Sum
# Language: python3
# Runtime: 50 ms
# Memory: 17.4 MB

class Solution:
    def missingInteger(self, A: List[int]) -> int:
        N = len(A)
        ans = lans = A[0]
        for j in range(1,N):
            if A[j] == A[j-1] + 1:
                ans += A[j]
            else:
                break
        S = set(A)
        x = ans
        while x in S:
            x += 1
        
        return x