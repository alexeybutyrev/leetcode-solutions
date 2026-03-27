# Problem: Minimum Operations to Convert All Elements to Zero
# Language: python3
# Runtime: 206 ms
# Memory: 29.8 MB

class Solution:
    def minOperations(self, A: List[int]) -> int:
        stack = []

        ans = 0
        for x in A:
            while stack and stack[-1] > x:
                stack.pop()

            if not x: continue
            if not stack or stack[-1] < x:
                ans += 1
                stack.append(x)
        return ans
