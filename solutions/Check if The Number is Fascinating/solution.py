# Problem: Check if The Number is Fascinating
# Language: python3
# Runtime: 53 ms
# Memory: 16.4 MB

class Solution:
    def isFascinating(self, n: int) -> bool:
        #print(str(n) + str(2*n) + str(3*n))
        s = Counter((str(n) + str(2*n) + str(3*n)))
        if '0' in s:
            return False
        for x in '123456789':
            if x not in s or s[x] > 1:
                return False
        return True