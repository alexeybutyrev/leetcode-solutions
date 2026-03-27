# Problem: Clear Digits
# Language: python3
# Runtime: 39 ms
# Memory: 16.4 MB

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for x in s:
            if x.isnumeric():
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        return "".join(stack)
                
            