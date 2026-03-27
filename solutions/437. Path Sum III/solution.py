# Problem: Path Sum III
# Language: python3
# Runtime: 704 ms
# Memory: 15.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        q = deque([(root.val, root)])
        ans = 0
        seen = {root}
        while q:
            s, node = q.popleft()
            
            if s == targetSum:
                ans += 1
            
            if node.left:
                if node.left not in seen:
                    seen.add(node.left)
                    q.append((node.left.val, node.left))
                q.append((s + node.left.val, node.left))
            
            if node.right:
                if node.right not in seen:
                    seen.add(node.right)
                    q.append((node.right.val, node.right))
                q.append((s + node.right.val, node.right))
        
        return ans
            