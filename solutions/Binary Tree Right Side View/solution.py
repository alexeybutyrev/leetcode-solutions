# Problem: Binary Tree Right Side View
# Language: python3
# Runtime: 30 ms
# Memory: 13.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            L = len(q)
            for i in range(L):
                node = q.popleft()
                if i == L - 1:
                    ans.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return ans