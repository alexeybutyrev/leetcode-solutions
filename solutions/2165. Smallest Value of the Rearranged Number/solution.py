# Problem: Smallest Value of the Rearranged Number
# Language: python3
# Runtime: 44 ms
# Memory: 13.8 MB

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num ==0:
            return 0
        if num < 0:
            num *= -1
            s = list(str(num))
            s.sort(reverse = True)
            return -int("".join(s))
        else:
            s = str(num)
            N = len(s)
            s = s.replace('0','')
            NS = len(s)
            s = list(s)
            s.sort()
            return int(s[0] + (N - NS) * '0' + "".join(s[1:]))
            