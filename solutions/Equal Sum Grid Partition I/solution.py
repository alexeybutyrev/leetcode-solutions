# Problem: Equal Sum Grid Partition I
# Language: python3
# Runtime: 71 ms
# Memory: 46.9 MB

class Solution:
    def canPartitionGrid(self, A: List[List[int]]) -> bool:
        
        def check(grid):
            A = []
            for x in grid:
                A.append(sum(x))
            
            S = sum(A)

            s = 0
            for x in A:
                s += x
                if S - s == s: return True
            return False
        

        return check(A) or check(zip(*A))