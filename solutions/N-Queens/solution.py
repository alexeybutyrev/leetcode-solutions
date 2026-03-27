# Problem: N-Queens
# Language: python3
# Runtime: 138 ms
# Memory: 14.8 MB

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        ans = []
        
        def convert(queens):
            A = [["."] * n for _ in range(n)]
            for i,j in queens:
                
                A[i][j] = "Q"
            return map(lambda x: "".join(x), A)
        
        def add_queen(s, i,j):
            for k in range(n):
                s.add((i,k))
                s.add((k,j))
            k = 0
            while i + k < n and j + k < n:
                s.add((i+k,j+k))
                k+=1
            
            k = 0
            while i - k >= 0 and j - k >= 0:
                s.add((i-k,j-k))
                k+=1
            k = 0
            while i - k >= 0 and j + k < n:
                s.add((i-k,j+k))
                k+=1
            k = 0
            while i + k < n and j - k >= 0:
                s.add((i+k,j-k))
                k+=1
            
            return s
                
        def backtrack(i, queens, seen):
            if i == n:
                ans.append(convert(queens))
            else:
                for j in range(n):
                    if (i,j) not in seen:
                        s = {(i,j)}
                        s = add_queen(s, i,j)
                        backtrack(i+1, queens | {(i,j)}, seen | s)
        
        backtrack(0,set(),set())
        return ans