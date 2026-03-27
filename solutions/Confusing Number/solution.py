# Problem: Confusing Number
# Language: python3
# Runtime: 22 ms
# Memory: 13.9 MB

class Solution:
    def confusingNumber(self, n: int) -> bool:
        s = str(n)
        if any(d in s for d in '23457'):
            return False
        s2 = s[::-1]
        s3 = ''
        hm = {'6':'9','9':'6','1':'1','8':'8','0':'0'}
        for l in s2:
            s3+=hm[l]
        return s3!=s
            