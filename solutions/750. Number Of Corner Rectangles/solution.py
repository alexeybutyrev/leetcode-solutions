# Problem: Number Of Corner Rectangles
# Language: python3
# Runtime: 1056 ms
# Memory: 17 MB

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        
        # == grid[i][j + d] == grid[i+d][j+d] == grid[i+d][j] == 1
        count = 0
        c = Counter()
        
        for i in range(N):
            ones = []
            for j in range(M):
                if grid[i][j]:
                    for ind in ones:
                        count += c[(ind,j)]
                        c[(ind,j)] += 1
                    ones.append(j)
            
                

        return count 