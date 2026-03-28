# Problem: Repeated DNA Sequences
# Language: python3
# Runtime: 60 ms
# Memory: 24.4 MB

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        n = len(s)
        if len(s) <= 10:
            return []
        
        a = 4
        L = 10
        d = {"A":0, "C":1, "G": 2, "T": 3}
        nums = [d.get(l) for l in s]

        aL = a ** L
        
        h = 0
        seen = set()
        res = set()
        for i in range(n - L+1):
            if i > 0:
                h = h * a - nums[i-1] * aL + nums[i+L-1]
            else:
                for i in range(L):
                    h = h * a + nums[i]
            if h in seen:
                res.add(s[i:i+L])
            seen.add(h)
        
        return res
    