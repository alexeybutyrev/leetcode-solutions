# Problem: Find All The Lonely Nodes
# Language: python3
# Runtime: 144 ms
# Memory: 15.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        c = Counter()
        p = Counter()
        parent = {}
        def walk(node):
            if node:
                if node.left:
                    c[node.left] += 1
                    p[node] += 1
                    parent[node.left] = node
                    walk(node.left)
                    
                if node.right:
                    c[node.right] += 1
                    p[node] += 1
                    parent[node.right] = node
                    walk(node.right)
        
        walk(root)
        for node in c:
            if p[parent[node]] == 1:
                ans.append(node.val)
        
        return ans
                
            
                    
                    
                    
                    