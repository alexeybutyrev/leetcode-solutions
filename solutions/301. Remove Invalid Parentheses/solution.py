# Problem: Remove Invalid Parentheses
# Language: python3
# Runtime: 104 ms
# Memory: 14.6 MB

class Solution:
    def removeInvalidParentheses(self, T: str) -> List[str]:
        def is_valid(s):
            c = 0
            for l in s:
                if l == ")":
                    c -= 1
                    if c < 0:
                        return False
                elif l == "(":
                    c += 1
            
            return c == 0
        
        
        T = T.lstrip(")").rstrip("(")
        
        level = {T}
        
        while True:
            ans = list(filter(is_valid,level))
            
            if ans:
                return ans
            
            level = { s[:i] + s[i+1:] for s in level for i in range(len(s))}
        
        
       
                    
                    