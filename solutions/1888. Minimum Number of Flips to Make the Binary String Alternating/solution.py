# Problem: Minimum Number of Flips to Make the Binary String Alternating
# Language: python3
# Runtime: 636 ms
# Memory: 17.8 MB

class Solution:
    def minFlips(self, s: str) -> int:
        
        n = len(s)
        ans = n
        A = list(map(int, s + s))
        
        cur = 0
        for i in range(n-1):
            cur += A[i] != (i & 1)
        
        for i in range(n-1, 2 *n ):
            cur += A[i] != (i&1)
            if i >= n:
                cur -= A[i] != ((i-n) & 1)
            ans = min(ans, cur, n - cur)
        return ans
    
    