# Problem: Check Knight Tour Configuration
# Language: python3
# Runtime: 73 ms
# Memory: 13.9 MB

class Solution:
    def checkValidGrid(self, A: List[List[int]]) -> bool:
        N = len(A)
        def moves():
            return [(1,2),(-1,2), 
                   (1,-2),(-1,-2),
                   (2,1),(-2,1),
                   (2,-1),(-2,-1)]
        
        q = [(0,0)]
        

        count = 0
        for i,j in q:

            count += 1
            for dx,dy in moves():
                x = i + dx
                y = j + dy
                if 0 <= x < N and 0 <= y < N and A[x][y] == count:
                    q.append((x,y))
                    break
            else:

                return count == N * N

        return count == N * N