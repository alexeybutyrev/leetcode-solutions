# Problem: Flower Planting With No Adjacent
# Language: python3
# Runtime: 452 ms
# Memory: 21.4 MB

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u,v in paths:
            graph[u-1].add(v-1)
            graph[v-1].add(u-1)
        res = [0] * n
        for i in range(n):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in graph[i]}).pop()
        return res        