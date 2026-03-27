# Problem: Average of Levels in Binary Tree
# Language: python3
# Runtime: 44 ms
# Memory: 16.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q = deque([root])
        
        ans = []
        while q:
            l = len(q)
            s = 0
            count = 0
            for _ in range(l):
                node = q.popleft()
                count += 1
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(s / count)
        return ans