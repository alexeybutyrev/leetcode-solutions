# Problem: Minimum Genetic Mutation
# Language: python3
# Runtime: 47 ms
# Memory: 14 MB

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        s = set(bank)
        if end == start:
            return 0
        
        if end not in s:
            return -1
        
        
        s.discard(start)
        s.discard(end)
        
        s = [start] + list(s) + [end]
        N = len(s)
        
        def hamming(A,B):
            return sum( a != b for a,b in zip(A,B))
        
        graph = defaultdict(list)
        
        for i in range(N):
            for j in range(i+1,N):
                
                if hamming(s[i], s[j]) == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        #print(graph)
        l = 0
        q = deque([0])
        seen = {0}
        while q:
            L = len(q)
            for _ in range(L):
                node = q.popleft()
                if node == N-1:
                    return l
                for nb in graph[node]:
                    if nb not in seen:
                        seen.add(nb)
                        q.append(nb)
            l += 1
        
        return -1
            