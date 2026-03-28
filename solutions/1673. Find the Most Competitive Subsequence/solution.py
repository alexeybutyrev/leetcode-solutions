# Problem: Find the Most Competitive Subsequence
# Language: python3
# Runtime: 1404 ms
# Memory: 27.2 MB

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        N = len(nums)
        for i,n in enumerate(nums):
            if stack:
                if stack[-1] > n:
                    while stack and stack[-1] > n and len(stack) + N - i - 1 >= k:
                        stack.pop()
                    stack.append(n)
                else:
                    if len(stack) < k:
                        stack.append(n)
            else:
                stack.append(n)
        return stack