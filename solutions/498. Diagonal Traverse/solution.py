# Problem: Diagonal Traverse
# Language: python3
# Runtime: 192 ms
# Memory: 16.7 MB

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix
        n, m = len(matrix), len(matrix[0])
        
        count = 0
        i = j = 0
        res = []
        idown = True
        while count < m * n:
            #print(i,j)
            res.append(matrix[i][j])
            if idown:
                if i == 0 or j == m-1 :
                    if j == m-1:
                        i+=1
                    else:
                        j+=1
                        
                    idown = False
                else:
                    i-=1
                    j+=1
            else:
                if j == 0 or i == n-1:
                    if i == n-1:
                        j+=1  
                    else:
                        i+=1
                    idown = True
                else:
                    i+=1
                    j-=1
            count += 1
        return res