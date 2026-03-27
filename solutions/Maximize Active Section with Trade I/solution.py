# Problem: Maximize Active Section with Trade I
# Language: python3
# Runtime: 1385 ms
# Memory: 25.4 MB

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        def check(s):
            A = []
            c = s.count('1')
            ans =c
            for x,l in groupby(s):
                d = len(list(l))
                A.append((x,d))
            
            N = len(A)
            for i in range(1,N-1):
                if A[i-1][0] == A[i+1][0] == '0':
                    d = A[i-1][1] + A[i+1][1]
                    ans = max(ans, d + c)
            return ans
        
        return check(s)
        
            