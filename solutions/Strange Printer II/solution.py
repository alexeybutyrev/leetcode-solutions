# Problem: Strange Printer II
# Language: python3
# Runtime: 875 ms
# Memory: 14.4 MB

class Solution:
    def isPrintable(self, A: List[List[int]]) -> bool:
        bound = [ [61,61,-1,-1] for _ in range(61)]
        
        N, M = len(A), len(A[0])
        for i in range(N):
            for j in range(M):
                bound[A[i][j]][0] = min(bound[A[i][j]][0],i)
                bound[A[i][j]][1] = min(bound[A[i][j]][1],j)
                
                bound[A[i][j]][2] = max(bound[A[i][j]][2],i)
                bound[A[i][j]][3] = max(bound[A[i][j]][3],j)
        
        
        graph = defaultdict(set)
        inbound = [0] * 61
        for col in range(len(bound)):
            a,b,c,d = bound[col]
            
            for i in range(a,c+1):
                for j in range(b,d+1):
                    if A[i][j] != col and A[i][j] not in graph[col]:
                        graph[col].add(A[i][j])
                        inbound[A[i][j]] += 1
        

        q = []
        for node in range(61):
            if inbound[node] == 0:
                q.append(node)
                    
        for node in q:
            for nb in graph[node]:
                inbound[nb] -= 1
                if inbound[nb] == 0:
                    q.append(nb)

        return sum(inbound) == 0
        
        
        
        
        