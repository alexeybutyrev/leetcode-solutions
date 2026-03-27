# Problem: Find Nearest Right Node in Binary Tree
# Language: python3
# Runtime: 682 ms
# Memory: 51.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        q = deque([root])
        
        while q:
            L = len(q)
            for i in range(L):
                node = q.popleft()
                if i == L - 1 and node == u: return None
                if node == u: return q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return None
            