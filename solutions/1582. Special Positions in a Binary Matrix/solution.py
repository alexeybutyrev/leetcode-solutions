# Problem: Special Positions in a Binary Matrix
# Language: python3
# Runtime: 162 ms
# Memory: 16.7 MB

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n,m = len(mat), len(mat[0])
        
        count = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    pr = True
                    for k in range(n):
                        if k != i and mat[k][j] != 0:
                            pr = False
                            break
                    
                    for k in range(m):
                        if k != j and mat[i][k] != 0:
                            pr = False
                            break
                    if pr:
                        count+=1
                            
        
        
                
        return count
        
        
            