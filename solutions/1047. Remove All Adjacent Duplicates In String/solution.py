# Problem: Remove All Adjacent Duplicates In String
# Language: python3
# Runtime: 68 ms
# Memory: 14.9 MB

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for l in s:
            if stack and l == stack[-1]:
                stack.pop()
            else:
                stack.append(l)
        return "".join(stack)