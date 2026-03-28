# Problem: Regular Expression Matching
# Language: python3
# Runtime: 44 ms
# Memory: 14.7 MB

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N = len(s)
        M = len(p)
        @lru_cache(None)
        def dfs(i,j):
            if j >= M:
                return i == N
            else:
                
                if j < M - 1 and p[j+1] == "*":
                    before = p[j]
                    j += 1
                    if dfs(i,j+1):
                        return True
                    while i < N and (s[i] == before or before == "."):
                        if dfs(i+1,j+1):
                            return True
                        
                        i+=1
                    
                    return dfs(i, j+1 )
                else:
                    if i == N:
                        return False
                    if p[j] in {s[i],"."} and dfs(i+1,j+1):
                        return True
                    
                return False
                    
                        
                    
                
                
                
        
        return dfs(0,0)