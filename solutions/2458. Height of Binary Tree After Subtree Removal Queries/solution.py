# Problem: Height of Binary Tree After Subtree Removal Queries
# Language: python3
# Runtime: 3815 ms
# Memory: 202.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depth = {}
        
        @cache
        def walk(node, d):
            if node:
                l = walk(node.left, d+1)
                r = walk(node.right,d+1)
                depth[node.val] = max(l,r)
                return depth[node.val]
            else:
                return d
        
        walk(root,0)
        
        
        q = deque([root])
        levels = defaultdict(list)
        hm = {}
        l = 0
        while q:
            L = len(q)
            for _ in range(L):
                node = q.popleft()
                hm[node.val] = l
                heappush(levels[l], (-depth[node.val], node.val))
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            l += 1
        seen = {}
        ans = []
        for q in queries:
            if q not in seen:
                if len(levels[hm[q]]) == 1:
                    ans.append(hm[q]-1)
                else:
                    a = 0
                    x,node = heappop(levels[hm[q]])
                    if node == q:
                        x2,node2 = heappop(levels[hm[q]])
                        ans.append(-x2-1)
                        heappush(levels[hm[q]], (x2,node2))
                    else:
                        ans.append(-x-1)
                    heappush(levels[hm[q]], (x,node))
                        
                seen[q] = ans[-1]
            else:
                ans.append(seen[q])
        return ans
        