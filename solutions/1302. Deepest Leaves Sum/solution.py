# Problem: Deepest Leaves Sum
# Language: python3
# Runtime: 96 ms
# Memory: 17.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = deque([root])
        ans = 0
        while q:
            l = len(q)
            s = 0
            for _ in range(l):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    s += node.left.val
                if node.right:
                    q.append(node.right)
                    s += node.right.val
            
            if q:
                ans = s
            else:
                return ans
        
        return ans