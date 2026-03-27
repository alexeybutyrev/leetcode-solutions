# Problem: Decode String
# Language: python3
# Runtime: 24 ms
# Memory: 14.1 MB

class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        
        def decode(i):
            if i >= n:
                return (n,"")
            
            stack = ""
            while i < n:
                if s[i] == "]":
                    return (i+1,stack)
                
                if s[i].isdigit():
                    k = 0
                    while s[i] != "[":
                        k = k * 10 + int(s[i])
                        i += 1
                    
                    (i,to_add) = decode(i+1)
                    stack += k * to_add
                else:
                    stack += s[i]
                    i += 1
            
            return (n,stack)
        
        return decode(0)[1]
                
                