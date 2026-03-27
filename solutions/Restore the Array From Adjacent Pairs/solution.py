# Problem: Restore the Array From Adjacent Pairs
# Language: python3
# Runtime: 898 ms
# Memory: 67.1 MB

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inbound = Counter()
        for u,v in adjacentPairs:
            graph[v].append(u)
            graph[u].append(v)
        
        N = len(graph)
        for start in graph:
            if len(graph[start]) == 1:
                break
        ans = [start]
        seen = {start}
        q = [start]


        for node in q:
            for nb in graph[node]:
                if nb not in seen:
                    seen.add(nb)
                    q.append(nb)
                    ans.append(nb)
                        
        return ans
                        