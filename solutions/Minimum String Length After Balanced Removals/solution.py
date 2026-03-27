# Problem: Minimum String Length After Balanced Removals
# Language: python3
# Runtime: 39 ms
# Memory: 19.4 MB

class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        stack = []
        for x in s:
            if stack and stack[-1] != x:
                stack.pop()
            else:
                stack.append(x)
        return len(stack)