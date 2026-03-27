# Problem: Replace Non-Coprime Numbers in Array
# Language: python3
# Runtime: 1624 ms
# Memory: 31 MB

class Solution:
    def replaceNonCoprimes(self, A: List[int]) -> List[int]:
        #def lcm(a, b): return abs(a*b) // gcd(a, b)
        
        stack = []
        
        for a in A:
            stack.append(a)
            while len(stack) > 1:
                x = stack.pop()
                y = stack.pop()
                g = gcd(x,y)
                if 1 == g:
                    stack.append(y)
                    stack.append(x)
                    break
                else:
                    stack.append(x*y // g)
        return stack