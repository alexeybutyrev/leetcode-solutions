# Problem: Pascal's Triangle
# Language: python3
# Runtime: 28 ms
# Memory: 14.2 MB

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        A = [[1]]
        
        for i in range(numRows-1):
            r = [1]
            for i in range(1,len(A[-1])):
                r.append(A[-1][i-1] + A[-1][i])
            r.append(1)
            A.append(r)
        
        return A