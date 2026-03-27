# Problem: Create Binary Tree From Descriptions
# Language: python3
# Runtime: 1670 ms
# Memory: 29.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        graph = defaultdict(list)
        kids = set()
        for p,c,il in descriptions:
            graph[p].append((c,il))
            kids.add(c)
        
        def bt(node):
            t = TreeNode(node)
            for c,il in graph[node]:
                if il:
                    t.left = bt(c)
                else:
                    t.right = bt(c)
            return t
        
        for x in graph:
            if x not in kids:
                root = x
        return bt(root)