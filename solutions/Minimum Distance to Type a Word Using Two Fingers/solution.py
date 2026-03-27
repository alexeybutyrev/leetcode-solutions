# Problem: Minimum Distance to Type a Word Using Two Fingers
# Language: python3
# Runtime: 1508 ms
# Memory: 156.9 MB

class Solution:
    def minimumDistance(self, word: str) -> int:
        start = ord('A')
        letters = []
        m = 6
        for l in word:
            j = 0
            for i in range(ord('A'), ord('Z') + 1):
                if (i - ord('A')) % m == 0:
                    j += 1
                if chr(i) == l:
                    break
            letters.append( ( (i - ord('A')) % m , j-1 ) )
        
        def dist(i,j):
            return abs(letters[i][0] - letters[j][0]) + abs(letters[i][1] - letters[j][1])
        
        N = len(letters)
        @lru_cache(None)
        def dp(k, i, j, started):
            if k == N:
                return 0
            
            d1 = dist(k,i) + dp(k+1, k, j, started)
            if started:
                d2 = dist(k,j) + dp(k+1, i, k, started)
            else:
                d2 = dp(k+1, i, k, True)
        
            return min(d1, d2)
        
        return dp(0, 0, 0, False)