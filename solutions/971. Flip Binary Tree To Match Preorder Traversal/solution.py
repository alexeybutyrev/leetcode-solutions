# Problem: Flip Binary Tree To Match Preorder Traversal
# Language: python3
# Runtime: 40 ms
# Memory: 14.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, A: List[int]) -> List[int]:
        
        q = deque([root])
        
        ans = []
        ind = 0
        N = len(A)
        while q:
            l = len(q)
            node = q.pop()
            if node.val != A[ind]:
                return [-1]
            ind += 1
            if ind == N:
                return ans
            if node.left and node.left.val != A[ind]:
                ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            else:
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                

        return ans