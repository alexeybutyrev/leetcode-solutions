# Problem: Find the Child Who Has the Ball After K Seconds
# Language: python3
# Runtime: 33 ms
# Memory: 16.3 MB


class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        i = 0
        curr = 1
        while k:
            if i == n-1:
                curr = -1
            if i == 0:
                curr = 1
            k-=1
            i += curr
        return i