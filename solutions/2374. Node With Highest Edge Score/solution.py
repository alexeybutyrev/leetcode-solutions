# Problem: Node With Highest Edge Score
# Language: python3
# Runtime: 1391 ms
# Memory: 31.8 MB

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        graph = Counter()
        for i,x in enumerate(edges):
            graph[x] += i
        
        s = -1
        for i in range(len(edges)):
            if i in graph:
                if graph[i] > s:
                    ans = i
                    s = graph[i]
        return ans

        