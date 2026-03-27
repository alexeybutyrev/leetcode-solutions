# Problem: Course Schedule II
# Language: python3
# Runtime: 104 ms
# Memory: 15.7 MB

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = Counter()
        
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        ans = []
        stack = []
        for i in range(numCourses):
            if not indegree[i]:
                stack.append(i)
                ans.append(i)
        
        
        while stack:
            node = stack.pop()
            for nb in graph[node]:
                indegree[nb] -= 1
                if not indegree[nb]:
                    stack.append(nb)
                    ans.append(nb)
        
        return ans if len(ans) == numCourses else []