# Problem: Minimum Window Subsequence
# Language: python3
# Runtime: 355 ms
# Memory: 24.6 MB

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        
        graph = defaultdict(list)
        for i,x in enumerate(s1):
            graph[x].append(i)
                
        M = len(s2)
        
        def search(i,j):
            if j == M:
                return i
            ind = bisect_right(graph[s2[j]],i)
            if ind == len(graph[s2[j]]):
                return inf
            return search(graph[s2[j]][ind],j+1)
        
        d = inf
        ans = ""
        for i in graph[s2[0]]:
            r = search(i,1)
            if d > r - i + 1:
                ans = s1[i:r +1] 
                d = r - i + 1

        return ans
            