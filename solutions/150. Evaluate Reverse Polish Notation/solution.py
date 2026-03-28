# Problem: Evaluate Reverse Polish Notation
# Language: python3
# Runtime: 56 ms
# Memory: 14.6 MB

class Solution:
    def evalRPN(self, A: List[str]) -> int:
        #["2","1","+","3","*"]
        
        def apply(a,b,o):
            if o == "+":
                return a + b
            if o == "-":
                return a - b
            if o == "*":
                return a * b
            
            return int(a/b)
        
        stack = []
        for a in A:
            if a in {"+", "*", "/", "-"}:
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(apply(v1,v2, a))
            else:
                stack.append(int(a))
        
        return stack[-1]
            