# Problem: Best Meeting Point
# Language: python3
# Runtime: 120 ms
# Memory: 22.7 MB

class Solution:
    def minTotalDistance(self, A: List[List[int]]) -> int:
        ans = 0
        points = set()
        R,C = [],[]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    R.append(i)
                    C.append(j)
                    points.add((i,j))
        R.sort()
        C.sort()
        x = R[len(R)//2]
        y = C[len(C)//2]
        
        for i,j in points:
            ans += abs(x-i) + abs(y-j)
        return ans