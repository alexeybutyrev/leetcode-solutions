# Problem: Spiral Matrix II
# Language: python3
# Runtime: 24 ms
# Memory: 14.4 MB

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        M = [[0] * n for _ in range(n)]
 
        rs = 0
        re = n
        
        cs = 0
        ce = n
        
        rows = True
        right = True
        down = True
        
        count = 0
        while count < n * n:
            #print(count, rs, re, cs, ce)
            if rows:
                if right:
                    for j in range(cs, ce):
                        count += 1
                        M[rs][j] = count
                    rs += 1
                else:
                    for j in range(ce-1, cs-1, -1):
                        count += 1
                        M[re-1][j] = count
                    re -= 1
                
                right = not right
            else:
                if down:
                    for i in range(rs, re):
                        count += 1
                        M[i][ce-1] = count
                    ce -= 1
                else:
                    for i in range(re-1, rs-1,-1):
                        count += 1
                        M[i][cs] = count
                    cs += 1
                    
                down = not down
            rows = not rows
        
        return M