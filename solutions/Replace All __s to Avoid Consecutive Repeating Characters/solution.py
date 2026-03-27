# Problem: Replace All ?'s to Avoid Consecutive Repeating Characters
# Language: python3
# Runtime: 40 ms
# Memory: 13.8 MB

class Solution:
    def modifyString(self, s: str) -> str:
        
        n = len(s)
        if n == 0:
            return s
        
        s = list(s)
        for i in range(n):
            if s[i] == "?":
                if i == n-1:
                    if i == 0:
                        return 'a'
                    
                    for j in range(ord('a'), ord('z') + 1):
                        if ord(s[i-1]) != j:
                            s[i] = chr(j)
                            break
                elif i == 0:
                    if n == 1:
                        return 'a'
                    
                    for j in range(ord('a'), ord('z') + 1):
                        if ord(s[i+1]) != j:
                            s[i] = chr(j)
                            break
                else:
                    for j in range(ord('a'), ord('z') + 1):
                        if ord(s[i+1]) != j and ord(s[i-1]) != j:
                            s[i] = chr(j)
                            break
        
        return "".join(s)