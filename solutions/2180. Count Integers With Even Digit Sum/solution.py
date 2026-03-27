# Problem: Count Integers With Even Digit Sum
# Language: python3
# Runtime: 66 ms
# Memory: 13.9 MB

class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for a in range(1,num+1):
            s = sum(map(int,list(str(a))))
            if s & 1 == 0:
                ans += 1
        return ans
                    