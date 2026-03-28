# Problem: Slowest Key
# Language: python3
# Runtime: 48 ms
# Memory: 14.3 MB

class Solution:
    def slowestKey(self, A: List[int], keysPressed: str) -> str:
        N = len(A)
        A = [0] + A
        
        c = Counter()
        ans = ""
        md = -1
        for i in range(N):
            c[keysPressed[i]] = max(c[keysPressed[i]], A[i+1] - A[i])
            if c[keysPressed[i]] >= md:
                if c[keysPressed[i]] == md:
                    ans = max(ans, keysPressed[i])
                else:
                    ans = keysPressed[i]
                md = c[keysPressed[i]]
        
        return ans