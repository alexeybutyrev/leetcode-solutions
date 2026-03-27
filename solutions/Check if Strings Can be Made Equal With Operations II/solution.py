# Problem: Check if Strings Can be Made Equal With Operations II
# Language: python3
# Runtime: 291 ms
# Memory: 17.6 MB

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        c1o = Counter()
        c1e = Counter()
        
        c2o = Counter()
        c2e = Counter()
        
        for i in range(len(s1)):
            if i & 1:
                c1o[s1[i]] += 1
                c2o[s2[i]] += 1
            else:
                c1e[s1[i]] += 1
                c2e[s2[i]] += 1
        return c1o == c2o and c1e == c2e
                                
        