# Problem: Minimum Remove to Make Valid Parentheses
# Language: python
# Runtime: 1648 ms
# Memory: 16.8 MB

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        nl = 0
        for l in s:
            if l == ")":
                if nl:
                    nl -= 1
                    stack.append(")")
                else:
                    continue
            else:
                if l == "(":
                    nl += 1
                stack.append(l)
        ans = ""
        for l in stack[::-1]:
            if l == "(" and nl:
                nl-=1
            else:
                ans= l + ans
        
        return ans