# Problem: Jump Game IV
# Language: python3
# Runtime: 993 ms
# Memory: 29.2 MB

class Solution:
    def minJumps(self, A: List[int]) -> int:
        graph = defaultdict(list)
        path = defaultdict(list)
        N = len(A)
        for i,a in enumerate(A):
            path[a].append(i)
        
        q =  deque([0])
        seen = {0}
        count = 0
        while q:
            L = len(q)
            
            for _ in range(L):
                node = q.popleft()
                if node == N - 1:
                    return count
                for nb in path[A[node]]:
                    if nb not in seen:
                        seen.add(node)
                        q.append(nb)

                path[A[node]].clear()

                if node + 1 < N and node + 1 not in seen:
                    seen.add(node + 1)
                    q.append(node + 1)


                if node - 1 >= 0 and node - 1 not in seen:
                    seen.add(node - 1)
                    q.append(node - 1)            
            count += 1
            
        return 0
            