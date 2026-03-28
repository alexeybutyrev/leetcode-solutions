# Problem: Find Duplicate Subtrees
# Language: python3
# Runtime: 64 ms
# Memory: 27.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        pattern = defaultdict(list)
        def dfs(node):
            if node:
                key = str(node.val) + "("
                lk = dfs(node.left)
                rk = dfs(node.right)
                
                key += 'l' + lk + 'r' + rk + ")"
                pattern[key].append(node)
                return key
            else:
                return ""
        
        dfs(root)
        
        ans = []
        for k in pattern:
            if len(pattern[k]) > 1:
                ans.append(pattern[k][0])
        return ans