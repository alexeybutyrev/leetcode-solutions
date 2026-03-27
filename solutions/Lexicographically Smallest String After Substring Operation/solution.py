# Problem: Lexicographically Smallest String After Substring Operation
# Language: python3
# Runtime: 184 ms
# Memory: 21 MB

class Solution:
    def smallestString(self, s: str) -> str:
        
        for i in range(len(s)):
            if s[i] != 'a':
                break
        else:
            
            return s[:-1] + 'z'
        
        ans = 'a' * i
        for j in range(i,len(s)):
            if s[j] != 'a':
                ans += chr(ord(s[j]) - 1)
            else:
                return ans + s[j:]
        
        return ans
        
        
        