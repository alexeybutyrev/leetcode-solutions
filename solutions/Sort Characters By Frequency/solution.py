# Problem: Sort Characters By Frequency
# Language: python3
# Runtime: 33 ms
# Memory: 15.2 MB

class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        
        ans = ''
        for k,v in sorted(c.items(), key = lambda x: -x[1]):
            ans += k * v
        
        return ans
        