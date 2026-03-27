# Problem: Merge Adjacent Equal Elements
# Language: python3
# Runtime: 91 ms
# Memory: 32.6 MB

class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for x in nums:
            while stack and x == stack[-1]:
                x = x + stack.pop()
            stack.append(x)
        return stack