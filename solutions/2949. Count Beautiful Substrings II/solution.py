# Problem: Count Beautiful Substrings II
# Language: python3
# Runtime: 268 ms
# Memory: 20.6 MB

class Solution:
    def beautifulSubstrings(self, S: str, k: int) -> int:
        
        V = {'a', 'e', 'i', 'o', 'u'}
        ans = c = v = 0
        seen = Counter()
        seen[(0,0)] = 1
        
        i = 1
        while (i * i) % k != 0:
            i += 1
        
        for x in S:
            if x in V:
                v += 1
            else:
                c += 1
            
            
            k = (v % i, v - c)
            ans += seen[k]
            seen[k] += 1
        
        return ans