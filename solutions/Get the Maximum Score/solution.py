# Problem: Get the Maximum Score
# Language: python3
# Runtime: 880 ms
# Memory: 234.7 MB

class Solution:
    def maxSum(self, A1: List[int], A2: List[int]) -> int:
        MOD = 10**9 + 7
        N1 = len(A1)
        N2 = len(A2)
        
        hm1 = {a: i for i,a in enumerate(A1)}
        hm2 = {a: i for i,a in enumerate(A2)}
        @lru_cache(None)
        def walk(i, state):
            if (state == "top" and i == N1) or (state == "bottom" and i == N2):
                return 0
            
            ans = 0
            if state == "top":
                ans = max(ans, A1[i] + walk(i+1, state))
                if A1[i] in hm2:
                    ans = max(ans, A1[i] + walk(hm2[A1[i]]+1, "bottom"))
            else:
                ans = A2[i] + walk(i+1, state)
                
                if A2[i] in hm1:
                    ans =  max(ans, A2[i] + walk(hm1[A2[i]]+1, "top"))

            return ans
        
        
        s1 = walk(0,"top") % MOD
        s2 = walk(0,"bottom") % MOD

        return max(s1, s2)
        