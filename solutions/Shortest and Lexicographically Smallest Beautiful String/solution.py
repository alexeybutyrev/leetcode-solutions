# Problem: Shortest and Lexicographically Smallest Beautiful String
# Language: python3
# Runtime: 44 ms
# Memory: 16.2 MB

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        c = Counter()
        ans = ""
        d = inf
        N = len(s)
        i = 0
        for j in range(N):
            c[s[j]] += 1
            while c['1'] > k:
                c[s[i]] -= 1
                i += 1
            while i < j and s[i] == '0':
                i+= 1
            
            if c['1'] == k and d >= j - i + 1:
                if d > j - i + 1:
                    ans = s[i:j+1]
                else:
                    ans = min(s[i:j+1], ans)
                d = j - i + 1
                
        
        return ans
                