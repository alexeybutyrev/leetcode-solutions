# Problem: Minimum Remove to Make Valid Parentheses
# Language: python3
# Runtime: 80 ms
# Memory: 17.9 MB

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        c = Counter(s)
        l = 0
        r = c[")"]
        ans = ""
        for a in s:
            if a == ")":
                r -= 1
                if l == 0:
                    continue
                l-=1
                ans += a
            elif a == "(":
                if l >= r:
                    continue
                l += 1
                ans += a
                    
            else:
                ans += a
                
        return ans