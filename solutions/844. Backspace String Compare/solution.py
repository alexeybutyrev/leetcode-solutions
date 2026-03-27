# Problem: Backspace String Compare
# Language: python3
# Runtime: 32 ms
# Memory: 14.3 MB

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def clear(S):
            stack = []
            
            for l in S:
                if l == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(l)
            
            return "".join(stack)
        return clear(S) == clear(T)
            