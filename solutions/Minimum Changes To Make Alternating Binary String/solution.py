# Problem: Minimum Changes To Make Alternating Binary String
# Language: python3
# Runtime: 7 ms
# Memory: 19.3 MB

class Solution:
    def minOperations(self, s: str) -> int:
        a = 0
        b = 0

        for i,x in enumerate(s):
            if i & 1:
                if x == '0':
                    a +=1
                else:
                    b += 1
            else:
                if x == '1':
                    a +=1
                else:
                    b += 1
        return min(a,b)