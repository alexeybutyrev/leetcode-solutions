# Problem: Minimum Number of Visited Cells in a Grid
# Language: python3
# Runtime: 3829 ms
# Memory: 53.7 MB

class Solution:
    def minimumVisitedCells(self, A: List[List[int]]) -> int:
        graph = defaultdict(list)
        N = len(A)
        M = len(A[0])
        
        q = deque([(0,0)])
        seen = {(0,0)}
        
        
        l = 1
        while q:
            L = len(q)
            for _ in range(L):
                i, j = q.popleft()
                if i == N-1 and j == M-1: return l
                for k in range(j+1, A[i][j] + j+1):
                    if k >= M: break
                    if i == N-1 and k == M-1: return l+1
                    if (i,k) not in seen:
                        seen.add((i,k))
                        q.append((i,k))


                for k in range(i+1, A[i][j] + i+1):
                    if k >= N: break
                    if k == N-1 and j == M-1: return l+1
                    if (k,j) not in seen:
                        seen.add((k,j))
                        q.append((k,j))
                        
                
            l+=1
            
            
        return -1
                