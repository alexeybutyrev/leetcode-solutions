# Problem: Candy Crush
# Language: python3
# Runtime: 155 ms
# Memory: 16.2 MB

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        A = list(zip(*board))
        N, M = len(A), len(A[0])
        
        def fix(A, mask):
            ans = []
            for i,l in enumerate(A):
                n_ones = mask[i].count(1)
                B = [0] * n_ones
                for j in range(M):
                    if mask[i][j] == 0:
                        B.append(A[i][j])
                ans.append(B)
            return ans
        
        
        def check(mask):
            seen = False
            for i in range(N):
                j = 0
                while j < M-2:
                    if j < M - 2 and A[i][j] and A[i][j] == A[i][j+1] == A[i][j+2]:
                        count = 2
                        mask[i][j] = mask[i][j+1] = 1
                        seen = True
                        while j < M - 2 and A[i][j] and A[i][j] == A[i][j+1] == A[i][j+2]:
                            mask[i][j+2] = 1
                            count += 1
                            j += 1
                    else:
                        j+=1
            
            for j in range(M):
                i = 0
                while i < N-2:
                    if i < N - 2 and A[i][j] and A[i][j] == A[i+1][j] == A[i+2][j]:
                        count = 2
                        mask[i][j] = mask[i+1][j] = 1
                        seen = True
                        while i < N - 2 and A[i][j] and A[i][j] == A[i+1][j] == A[i+2][j]:
                            mask[i+2][j] = 1
                            count += 1
                            i += 1
                    else:
                        i += 1
            return seen, mask
                        
                        
        seen = True        
        while seen:
            seen = False
            mask = [[0] * M for _ in range(N)]
            seen, mask = check(mask)
            
            if seen:
                A = fix(A, mask)

        
        return list(zip(*A))
            
                    
                        
            
            