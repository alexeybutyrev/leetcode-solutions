# Problem: Island Perimeter
# Language: python3
# Runtime: 532 ms
# Memory: 12.9 MB

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        # add zero layer
        for i in range(len(grid)):
            grid[i] = [0] + grid[i] + [0]
        
        grid = [[0] * len(grid[0])] + grid + [[0] * len(grid[0])]
        
        p = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if 1 == grid[i][j]:
                    p+= 4
                    p = p - (grid[i-1][j] + grid[i+1][j] + grid[i][j-1] + grid[i][j+1])
                    
                        
        
        return p