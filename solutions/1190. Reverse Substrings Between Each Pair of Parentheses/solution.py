# Problem: Reverse Substrings Between Each Pair of Parentheses
# Language: python3
# Runtime: 33 ms
# Memory: 16.5 MB

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for x in s:
            if x == ')':
                s0 = ''
                while stack and stack[-1] != '(':
                    s0 += stack.pop()
                stack.pop()
                for x1 in s0:
                    stack.append(x1)
            else:
                stack.append(x)
        
        return "".join(stack)