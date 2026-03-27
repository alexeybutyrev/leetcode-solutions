# Problem: Count Beautiful Substrings I
# Language: python3
# Runtime: 1423 ms
# Memory: 16.3 MB

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        V = {'a', 'e', 'i', 'o', 'u'}
        v,c=0,0
        i = 0
        N = len(s)
        ans = 0
        for i in range(N):
            v = c = 0
            for j in range(i,N):
                x = s[j]
                if x in V:
                    v += 1
                else:
                    c += 1
            
                if v and v == c and (v * c) % k == 0:
                    ans += 1
            
        return ans