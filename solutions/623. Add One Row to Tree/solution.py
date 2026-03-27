# Problem: Add One Row to Tree
# Language: python3
# Runtime: 120 ms
# Memory: 16.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            n = TreeNode(val)
            n.left = root
            return n
        
        q = deque([root])
        level = 1
        while q:
            L = len(q)
            if level == depth - 1:
                for _ in range(L):
                    node = q.popleft()
                    n = TreeNode(val)
                    n.left = node.left
                    node.left = n
                    q.append(n)
                    
                    n = TreeNode(val)
                    n.right = node.right
                    node.right = n
                    q.append(n)
            else:
                for _ in range(L):
                    node = q.popleft()
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            level += 1
        
        return root