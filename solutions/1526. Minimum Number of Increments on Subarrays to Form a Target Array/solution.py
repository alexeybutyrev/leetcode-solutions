# Problem: Minimum Number of Increments on Subarrays to Form a Target Array
# Language: python3
# Runtime: 23 ms
# Memory: 26.7 MB

class Solution:
    def minNumberOperations(self, A: List[int]) -> int:
        ans = 0
        b = 0

        for x in A:
            if x > b:
                ans += x - b
            b = x
        return ans


