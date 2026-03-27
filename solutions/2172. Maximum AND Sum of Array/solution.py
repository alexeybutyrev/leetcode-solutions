# Problem: Maximum AND Sum of Array
# Language: python3
# Runtime: 664 ms
# Memory: 24 MB

class Solution:
    def maximumANDSum(self, A: List[int], NS: int) -> int:
        
        N = len(A)
        @cache
        def dp(i,s1,s2):
            if i == N:
                return 0
            else:
                ans = 0
                for s in range(1,NS+1):
                    if (s1 & (1 <<(s-1))) == 0:
                        ans = max(ans, (A[i] & s) + dp(i+1, s1 | (1 <<(s-1)), s2))
                    else:
                        if (s2 & (1 <<(s-1))) == 0:
                            ans = max(ans, (A[i] & s) + dp(i+1, s1 , s2 | (1 <<(s-1))))
                #print(ans)
                return ans
        
        return dp(0,0,0)