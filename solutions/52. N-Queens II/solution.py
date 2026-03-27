# Problem: N-Queens II
# Language: python3
# Runtime: 44 ms
# Memory: 14.1 MB

class Solution:
    def totalNQueens(self, n):
        def dfs(i, c1, c2, c3):
            if i == n: self.ans += 1
            
            for j in range(n):
                if c1 & 1<<j or c2 & 1<<i-j+n or c3 & 1<<i+j: continue
                dfs(i + 1, c1 ^ 1<<j, c2 ^ 1<<i-j+n, c3 ^ 1<<i+j)
        
        self.ans = 0
        dfs(0, 0, 0, 0)
        return self.ans