# Problem: Binary Tree Zigzag Level Order Traversal
# Language: python3
# Runtime: 0 ms
# Memory: 17.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root: return ans
        q = deque([root])
        while q:
            L = len(q)
            a = []
            for _ in range(L):
                
                node = q.popleft()
                a.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            ans.append(a)
            if len(ans) & 1 == 0:
                ans[-1] = ans[-1][::-1]
        return ans
                