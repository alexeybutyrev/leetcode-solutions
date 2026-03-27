# Problem: Long Pressed Name
# Language: python3
# Runtime: 28 ms
# Memory: 14.3 MB

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        stack = ""
        M = len(typed)
        N = len(name)
        i = j = 0
        while i < N and j < M:
            if name[i] != typed[j]:
                while j < M and stack and typed[j] == stack[-1]:
                    j += 1
                    
                if j == M or name[i] !=typed[j]:
                    return False
            
            stack += name[i]
            
            i+=1
            j += 1
        
        if i < N:
            return False
        
        while j < M and stack and typed[j] == stack[-1]:
            j += 1
        
        return j == M