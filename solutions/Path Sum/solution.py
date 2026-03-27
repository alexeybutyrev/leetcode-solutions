# Problem: Path Sum
# Language: python
# Runtime: 36 ms
# Memory: 15.5 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _hasPS(self, node, sm_, target):
        sm_ += node.val
        print(sm_, node.val, target)
        if not node.left and not node.right:
            print("here")
            if sm_ == target: 
                print("here2")
                return True
            
        if node.left:
            return self._hasPS(node.left, sm_, target)
        if node.right:
            return self._hasPS(node.right, sm_, target)
            
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
    
    