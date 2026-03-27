# Problem: Removing Stars From a String
# Language: python3
# Runtime: 244 ms
# Memory: 15.6 MB

class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []
        for l in s:
            if l == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(l)
        return "".join(stack)