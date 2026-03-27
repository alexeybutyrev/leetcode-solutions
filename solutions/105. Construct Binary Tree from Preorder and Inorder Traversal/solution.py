# Problem: Construct Binary Tree from Preorder and Inorder Traversal
# Language: python3
# Runtime: 150 ms
# Memory: 53.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, P: List[int], I: List[int]) -> Optional[TreeNode]:
        N = len(P)
        
        def walk(P,I):
            if not P or not I:
                return None
            
            val = P.popleft()
            t = TreeNode(val)
            ind = I.index(val)
            t.left  = walk(P,I[:ind])
            t.right = walk(P,I[ind+1:])
            return t
    
        return walk(deque(P),I)