# Problem: Filling Bookcase Shelves
# Language: python3
# Runtime: 44 ms
# Memory: 15.9 MB

class Solution:
    def minHeightShelves(self, A: List[List[int]], shelf_width: int) -> int:
        N = len(A)
        
        @cache
        def dfs(i, sw, h):
            if i == N:
                return h
            
            a1 = inf    
            if sw >= A[i][0]:
                a1 = dfs(i+1, sw - A[i][0], max(h,A[i][1]))

            a2 = h + dfs(i+1, shelf_width - A[i][0], A[i][1])
            return min(a1,a2)
        
        return dfs(0,shelf_width, 0)
                            