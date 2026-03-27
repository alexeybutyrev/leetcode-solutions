# Problem: Maximum Score From Removing Substrings
# Language: python3
# Runtime: 332 ms
# Memory: 18.5 MB

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        if x < y:    
        
            ns = []
            ans = 0
            for e in s:

                ns.append(e)

                while len(ns) > 1 and ns[-2] == "b" and ns[-1] == "a":
                    ns.pop()
                    ns.pop()
                    ans += y

            stack = []
            for e in ns:

                stack.append(e)

                while len(stack) > 1 and stack[-2] == "a" and stack[-1] == "b":
                    stack.pop()
                    stack.pop()
                    ans += x
        else:
            ns = []
            ans = 0
            for e in s:

                ns.append(e)

                while len(ns) > 1 and ns[-2] == "a" and ns[-1] == "b":
                    ns.pop()
                    ns.pop()
                    ans += x

            stack = []
            for e in ns:

                stack.append(e)

                while len(stack) > 1 and stack[-2] == "b" and stack[-1] == "a":
                    stack.pop()
                    stack.pop()
                    ans += y

        return ans
        
        
            