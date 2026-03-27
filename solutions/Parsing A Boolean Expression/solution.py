# Problem: Parsing A Boolean Expression
# Language: python3
# Runtime: 52 ms
# Memory: 14.5 MB

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        func = {'&' : all, '|' : any, '!' : lambda x : not x[0]}
        
        stack = []
        for c in expression:
            if c in func:
                stack.append(func[c])
            elif c == '(':
                stack.append('(')
            elif c == 'f':
                stack.append(False)
            elif c == 't':
                stack.append(True)
                
            elif c == ')':
                ss = []
                while stack[-1] != '(':
                    ss.append(stack.pop())
                stack.pop()
                stack.append(stack.pop()(ss))

        return stack.pop()