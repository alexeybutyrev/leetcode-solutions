# Problem: Valid Parentheses
# Language: python
# Runtime: 24 ms
# Memory: 11.9 MB

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ins, outs = ["(", "[", "{"], [")", "]", "}"]
        
        hm = dict()
        res = dict(zip(outs, ins))
        
        stack = []
        for v in s:
            if v in ins:
                stack.append(v)
                
            if v in outs:
                if len(stack) > 0:
                    last = stack.pop()
                    if last != res[v]:
                        return False
                else:
                    return False
        if stack:
            return False
        
        return True
    