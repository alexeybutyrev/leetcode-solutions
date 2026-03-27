# Problem: Sort Matrix by Diagonals
# Language: python3
# Runtime: 12 ms
# Memory: 18 MB

class Solution:
    def sortMatrix(self, A: List[List[int]]) -> List[List[int]]:
        N, M = len(A), len(A[0])

        d = defaultdict(list)

        for i in range(N):
            l = []
            j = 0
            for x in range(N):
                if i + x == N:
                    break
                l.append(A[i+x][j+x])
            l.sort()
            for x in range(N):
                if i+x == N or j + x == N:
                    break
                A[i+x][j+x] = l.pop()
        
        for j in range(1,N):
            l = []
            i = 0
            for x in range(N):
                if i+x == N or j + x == N:
                    break
                l.append(A[i+x][j+x])
            l.sort(reverse = True)
            for x in range(N):
                if j + x == N:
                    break
                A[i+x][j+x] = l.pop()
        
        return A