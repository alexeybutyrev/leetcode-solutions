# Problem: Max Increase to Keep City Skyline
# Language: python3
# Runtime: 156 ms
# Memory: 27.3 MB

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        import numpy as np
        # convert to numpy to ease calcs
        G = np.array(grid)

        # find arrays to comapre
        top_bottom_max = np.max(G, axis=0)
        left_right_max = np.max(G, axis=1)

        # main loop
        total_increase = 0
        for row in range(G.shape[0]):
            for col in range(G.shape[1]):
                min_hgt = min(top_bottom_max[col], left_right_max[row])

                if G[row, col] < min_hgt:
                    total_increase += min_hgt - G[row, col]
                    G[row, col] = min_hgt
        return total_increase

