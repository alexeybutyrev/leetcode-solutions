# Problem: Beautiful Arrangement
# Language: python3
# Runtime: 1632 ms
# Memory: 14.3 MB

class Solution:
    def countArrangement(self, N: int) -> int:
        
        
        count = 0 
        visited = [False] * N
        
        def backtrack(visited,pos):
            nonlocal count
            
            if pos > N:
                count += 1
                                    
            for i in range(1,N+1):
                if not visited[i-1] and (i % pos == 0 or pos % i == 0):
                    visited[i-1] = True
                    backtrack(visited, pos + 1)
                    visited[i-1] = False

        backtrack(visited,1)
        return count
        
        