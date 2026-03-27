# Problem: Interleaving String
# Language: python3
# Runtime: 24 ms
# Memory: 14.6 MB

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        N,M,K=len(s1),len(s2),len(s3)
        
        if K != N + M:
            return False
        @lru_cache(None)
        def dfs(i,j):
            
            if i == N and j == M and i+j == K:
                return True
            
            t1 = False
            if i < N and s1[i] == s3[i+j]:
                t1 = dfs(i+1,j)
            
            t2 = False
            if j < M and s2[j] == s3[i+j]:
                t2 = dfs(i,j+1)
            
            return t1 | t2
        
        return dfs(0,0)
