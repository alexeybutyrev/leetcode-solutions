# Problem: Binary Tree Level Order Traversal
# Language: python3
# Runtime: 36 ms
# Memory: 14.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            L = len(q)
            to_add = []
            for _ in range(L):
                node = q.popleft()
                to_add.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            ans.append(to_add)
        
        return ans