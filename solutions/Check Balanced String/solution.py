# Problem: Check Balanced String
# Language: python3
# Runtime: 0 ms
# Memory: 16.7 MB

class Solution:
    def isBalanced(self, num: str) -> bool:
        x = 0
        y = 0
        for i in range(len(num)):
            if i & 1:
                x += int(num[i])
            else:
                y += int(num[i])
        return x == y