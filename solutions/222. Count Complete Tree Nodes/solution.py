# Problem: Count Complete Tree Nodes
# Language: python3
# Runtime: 64 ms
# Memory: 21.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        r = root
        d = 0
        while r.left:
            d += 1
            r = r.left
            
        
        if not d:
            return 1
        
        c = 0
        
        
        def exists(x, node):
            left, right = 0, 2**d - 1
            for _ in range(d):
                pivot = left + (right - left) // 2
                if x <= pivot:
                    node = node.left
                    right = pivot
                else:
                    node = node.right
                    left = pivot + 1
            return node is not None
        
        hi = 2 ** d - 1
        lo = 1
        while lo <= hi:
            mid = lo + (hi-lo) //2
            if exists(mid,root):
                lo = mid + 1
            else:
                hi = mid - 1
        
        return 2 **d -1 + lo