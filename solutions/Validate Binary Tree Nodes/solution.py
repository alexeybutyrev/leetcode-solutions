# Problem: Validate Binary Tree Nodes
# Language: python3
# Runtime: 320 ms
# Memory: 30.3 MB

class Solution:
    def validateBinaryTreeNodes(self, n: int, L: List[int], R: List[int]) -> bool:
        seen = set()
        
        
        def dfs(u):
            seen.add(u)
            if R[u] >= 0:
                if R[u] in seen or not dfs(R[u]):
                    return False
            
            if L[u] >= 0:
                if L[u] in seen or not dfs(L[u]):
                    return False
            return True
        
        c = Counter(L)
        c += Counter(R)
        for i in range(n):
            if not c[i]:
                ans = dfs(i)
                return ans and len(seen) == n
        
            