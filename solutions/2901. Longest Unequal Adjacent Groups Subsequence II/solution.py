# Problem: Longest Unequal Adjacent Groups Subsequence II
# Language: python3
# Runtime: 1685 ms
# Memory: 24.1 MB

class Solution:
    def getWordsInLongestSubsequence(self, n: int, A: List[str], G: List[int]) -> List[str]:
        graph = defaultdict(list)
        N = len(A)
        def hamming(a,b):
            if len(a) != len(b): return 0
            ans = 0
            for x,y in zip(a,b):
                if x != y:
                    ans += 1
            return ans
        
        q = []
        for i in range(N):
            for j in range(i+1,N):
                if hamming(A[i], A[j]) == 1 and G[i] != G[j]:
                    graph[i].append(j)
            q.append(([A[i]],i))
            
        @cache
        def dfs(i):
            ans = [A[i]]
            for node in graph[i]:
                a = [A[i]] + dfs(node)
                if len(a) > len(ans):
                    ans = a
            return ans
        
        ans = []
        for i in range(N):
            a = dfs(i)
            if len(a) > len(ans):
                ans = a
        
        return ans
                
            
                