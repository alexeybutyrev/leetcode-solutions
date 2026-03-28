# Problem: Path Sum III
# Language: python3
# Runtime: 736 ms
# Memory: 15.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        visited = set()
        def walk(node,s):
            nonlocal count
            s = s + node.val
            if s == sum:
                #print(node)
                #print("here")
                count +=1
                
            if node.left:
                walk(node.left,s)
                if node.left not in visited:
                    visited.add(node.left)
                    walk(node.left,0)
            if node.right:
                walk(node.right,s)
                if node.right not in visited:
                    visited.add(node.right)
                    walk(node.right,0)
        
        count = 0
        walk(root,0)
        return count