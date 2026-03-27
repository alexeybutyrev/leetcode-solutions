# Problem: Cyclically Rotating a Grid
# Language: python3
# Runtime: 188 ms
# Memory: 14.8 MB

class Solution:
    def rotateGrid(self, A: List[List[int]], k: int) -> List[List[int]]:
        N, M = len(A), len(A[0])
        
        Nlayers = min(N,M) // 2
        
        L = []
        for l in range(Nlayers):
            layer = []
            
            for j in range(l,M-l):
                layer.append(A[l][j])
            
            for i in range(l+1,N-l):
                layer.append(A[i][M-1-l])
            
            for j in range(M-2-l,l-1,-1):
                layer.append(A[N-l-1][j])
            
            for i in range(N-2-l,l,-1):
                layer.append(A[i][l])
            L.append(layer)
        
        for i,l in enumerate(L):
            n = len(l)
            knew = k % n
            L[i] = L[i][knew:] + L[i][:knew] 
        

        ANS = [[0] * M for _ in range(N)]
        
        for l in range(Nlayers):
            layer = L[l]
            
            k = 0
            for j in range(l,M-l):
                ANS[l][j] = layer[k]
                k+=1
            for i in range(l+1,N-l):
                ANS[i][M-1-l] = layer[k]
                k+=1
            
            for j in range(M-2-l,l-1,-1):
                ANS[N-l-1][j] = layer[k]
                k += 1
            for i in range(N-2-l,l,-1):
                ANS[i][l] = layer[k]
                k += 1
            
            
        return ANS
            