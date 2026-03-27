# Problem: Maximum Ascending Subarray Sum
# Language: python3
# Runtime: 3 ms
# Memory: 17.7 MB

class Solution:
    def maxAscendingSum(self, A: List[int]) -> int:
        ans = 0
        s = 0
        while A:
            s = x = A.pop()

            while A and A[-1] < x:
                x = A.pop()
                s += x
            ans = max(ans, s)
        return ans