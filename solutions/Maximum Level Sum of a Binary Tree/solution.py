# Problem: Maximum Level Sum of a Binary Tree
# Language: python3
# Runtime: 25 ms
# Memory: 21.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        
        ans = level = 0
        mx = -inf
        
        
        while q:
            level += 1
            curr_sum = 0
            L = len(q)
            for _ in range(L):
                node = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            if curr_sum > mx:
                mx = curr_sum
                ans = level
        return ans
        