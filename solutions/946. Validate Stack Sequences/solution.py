# Problem: Validate Stack Sequences
# Language: python3
# Runtime: 60 ms
# Memory: 14.5 MB

from collections import deque
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        N = len(pushed)
        
        stack = []
        i = 0
        for e in pushed:
            stack.append(e)
            while stack and stack[-1] == popped[i]:
                i += 1
                stack.pop()

        return i == N