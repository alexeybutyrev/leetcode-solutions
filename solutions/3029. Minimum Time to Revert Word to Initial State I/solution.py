# Problem: Minimum Time to Revert Word to Initial State I
# Language: python3
# Runtime: 37 ms
# Memory: 16.6 MB

class Solution:
    def minimumTimeToInitialState(self, W: str, k: int) -> int:
        
        def check(x,y):
            for a,b in zip(x,y):
                if b == "*":
                    continue
                if a != b: return False
            return True
        S = W
        ans = 0
        while True:
            ans += 1
            S = S[k:] + "*" * k
            if check(W,S):
                return ans
        
        return ans
            