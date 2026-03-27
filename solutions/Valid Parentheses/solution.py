# Problem: Valid Parentheses
# Language: python3
# Runtime: 4 ms
# Memory: 17.7 MB

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for l in s:
            if l == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif l == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif l == "}":
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)
        return not stack