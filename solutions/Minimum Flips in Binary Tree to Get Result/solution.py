# Problem: Minimum Flips in Binary Tree to Get Result
# Language: python3
# Runtime: 1286 ms
# Memory: 179.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        @cache
        def dp(node,target):
            if node.val in [0,1]: # leaf
                return 0 if node.val==target else 1
            elif node.val==5: # NOT
                return dp(node.left or node.right,1-target)
            if node.val==2: # OR
                nxt_targets = [[1,0],[0,1],[1,1]] if target==1 else [[0,0]]
            elif node.val==3: # AND
                nxt_targets = [[1,0],[0,1],[0,0]] if target==0 else [[1,1]]
            elif node.val==4: # XOR
                nxt_targets = [[1,0],[0,1]] if target==1 else [[0,0],[1,1]]
            return min(dp(node.left,t1)+dp(node.right,t2) for t1,t2 in nxt_targets)
        return dp(root,result)