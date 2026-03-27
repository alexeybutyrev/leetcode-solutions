# Problem: Score of Parentheses
# Language: python3
# Runtime: 24 ms
# Memory: 14.1 MB

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        
        for l in S:
            if l == "(":
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] +=  max(1, 2 *v)
        return stack[0]