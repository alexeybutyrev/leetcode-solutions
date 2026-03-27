# Problem:  Check if There Is a Valid Parentheses String Path
# Language: python3
# Runtime: 4985 ms
# Memory: 391.9 MB

class Solution:
    def hasValidPath(self, A: List[List[str]]) -> bool:
        @cache
        def is_valid(s):
            while "()" in s:
                s = s.replace("()","")
            return not s
        
        N, M = len(A), len(A[0])
        
        @cache
        def dfs(i,j,s):
            #print(i,j, N, M)
            
            s += A[i][j]
            if s.count(")") > s.count("("):
                return False
            
            while "()" in s:
                s = s.replace("()","")
                
            if i == N - 1 and j == M - 1:
                return is_valid(s)
            
            if i < N - 1:
                a = dfs(i+1,j, s)
                if a: 
                    return True
            if j < M - 1:
                return dfs(i,j+1,s)
        
        return dfs(0,0, "")