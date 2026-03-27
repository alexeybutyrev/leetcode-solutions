# Problem: Minimum Replacements to Sort the Array
# Language: python3
# Runtime: 460 ms
# Memory: 30.3 MB

class Solution:
    def minimumReplacement(self, A: List[int]) -> int:
        x = A[-1]
        ans = 0
        for a in A[:-1][::-1]:
            if a <= x:
                x = a
            else:
                c = (a + x - 1) // x
                ans += c -  1
                x = a // c
        return ans